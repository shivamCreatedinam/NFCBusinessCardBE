from abc import ABC

from rest_framework import serializers
from .models import User


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['mobile_number', 'otp', 'is_verified']


class OTPVerificationSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(max_length=10)
    otp = serializers.CharField(max_length=6)
