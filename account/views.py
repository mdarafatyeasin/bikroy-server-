from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import userRegistrationSerializer, userLoginSerializer
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from rest_framework.response import Response
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from rest_framework.authtoken.models import Token
from django.http import JsonResponse

# Create your views here.
# email confirm_link
def send_confirmation_email(user, confirm_link, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'confirm_link' : confirm_link,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()


# reg
class userRegistration(APIView):
    serializer = userRegistrationSerializer

    def post(self, request):
        serializer = self.serializer(data=request.data)

        if serializer.is_valid():
            user    = serializer.save()
            token   = default_token_generator.make_token(user)
            uid     = urlsafe_base64_encode(force_bytes(user.pk))

            confirm_link = f"http://127.0.0.1:8000/account/active/{uid}/{token}"
            send_confirmation_email(user,confirm_link, 'Email confirmation', 'confirm_email.html')
            return Response("Check your mail for confirmation")
        
        return Response(serializer.errors)
    
# confirm email to activate account
def activate(request, uid64, token):
    try: 
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid) 
    except(User.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return Response('http://localhost:5173/login')
    else:
        return Response('register')
    

# login 
class userLogin(APIView):
    def post(self,request):
        serializer = userLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                token,_ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'user': {'id': user.id, 'username': user.username}})
            else:
                return Response({'error':'Invalid user'})
        else:
            return Response(serializer.error)
        
# logout
def UserLogOut(request, id, token):
    try:
        user = User.objects.get(id=id)
        user_token = Token.objects.get(user=user).key
        if user:
            if token == user_token:
                current_token = Token.objects.get(user=user)
                logout(request)
                current_token.delete()
                return JsonResponse({'status': 'success'}, status=200)
            else:
                return JsonResponse({'status': 'token does not exist'})
    except (User.DoesNotExist, Token.DoesNotExist):
        return JsonResponse({'status': 'invalid user'})