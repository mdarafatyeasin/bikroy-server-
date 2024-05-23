from rest_framework import serializers
from account.models import basicInfo, additionalInfo, userInfo
from django.contrib.auth.models import User

class profileBasicInfo(serializers.ModelSerializer):
    class Meta:
        model = basicInfo
        exclude = ['profile_picture']
        read_only_fields = ['user']

class profileAdditionalInfo(serializers.ModelSerializer):
    class Meta:
        model = additionalInfo
        fields = "__all__"
        read_only_fields = ['user']

# class profileUserInfo(serializers.ModelSerializer):
#     class Meta:
#         model = userInfo
#         fields = "__all__"

class userProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        read_only_fields = ['id', 'username']