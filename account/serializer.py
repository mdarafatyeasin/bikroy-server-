from rest_framework import serializers
from .models import basicInfo, additionalInfo, userInfo
from django.contrib.auth.models import User
from adds.models import addModel

class BasicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = basicInfo
        fields = '__all__'

class AdditionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = additionalInfo
        fields = '__all__'

class UserInfoSerializer(serializers.ModelSerializer):
    basic_info = BasicInfoSerializer()
    additional_info = AdditionalInfoSerializer()

    class Meta:
        model = userInfo
        fields = '__all__'

class userRegistrationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=15) 
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'password', 'confirm_password']

    def create(self, validated_data):
        username            = validated_data['username']
        first_name          = validated_data['first_name']
        last_name           = validated_data['last_name']
        email               = validated_data['email']
        phone_number        = validated_data['phone_number']
        password            = validated_data['password']
        confirm_password    = validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({"error": "Password doesn't match"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "Email already exists"})

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        user.is_active = False
        user.save()


        basic_info          = basicInfo.objects.create(user=user, phone_number=phone_number)
        additional_info     = additionalInfo.objects.create(user=user)
        user_info           = userInfo.objects.create(user=user, basicInfo=basic_info, additionalInfo=additional_info)

        return user 

class userLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    class Meta:
        fields = ['username', 'password']

