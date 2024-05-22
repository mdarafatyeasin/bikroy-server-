from rest_framework import serializers
from .models import addModel

class addSerializer(serializers.ModelSerializer):
    class Meta:
        model   = addModel
        fields  = "__all__"