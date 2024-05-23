from .serializer import profileBasicInfo, profileAdditionalInfo, userProfileSerializer
from account.models import basicInfo, additionalInfo
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status, response
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from adds.models import addModel
from adds.serializers import addSerializer
from django.http import JsonResponse


class basicInfoViewset(APIView):
     def get_object(self, id):
        try:
            user = User.objects.get(pk=id)
            return basicInfo.objects.get(user=user)
        except User.DoesNotExist:
            raise Http404("User not found")
        except basicInfo.DoesNotExist:
            raise Http404("Basic info not found")
        
     def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = profileBasicInfo(snippet)
        return Response(serializer.data)
     
     def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = profileBasicInfo(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class additionalProfileInfo(APIView):
    def get_object(self, id):
        try:
            user = User.objects.get(pk=id)
            return additionalInfo.objects.get(user=user)
        except User.DoesNotExist:
            raise Http404("User not found")
        except additionalInfo.DoesNotExist:
            raise Http404("Basic info not found")
        
    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = profileAdditionalInfo(snippet)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = profileAdditionalInfo(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class additionalProfileInfo(generics.RetrieveUpdateAPIView):
#     queryset = additionalInfo.objects.all()
#     serializer_class = profileAdditionalInfo
#     lookup_field = 'id'

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()

#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         return response.Response({
#             'message': 'update success',
#             'updated_data': serializer.data
#         }, status=status.HTTP_200_OK)

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = userProfileSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return response.Response({
            'message': 'update success',
            'updated_data': serializer.data
        }, status=status.HTTP_200_OK)
    
def userAdds(request, id):
    products = addModel.objects.filter(author=id)
    serializer = addSerializer(products, many=True)  
    return JsonResponse(serializer.data, safe=False)  
