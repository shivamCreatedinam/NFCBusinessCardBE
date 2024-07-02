# from abc import ABC
#
# from rest_framework import serializers
# from .models import User
#
#
# class userSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['mobile_number', 'otp', 'is_verified']
#
#
# class OTPVerificationSerializer(serializers.Serializer):
#     mobile_number = serializers.CharField(max_length=10)
#     otp = serializers.CharField(max_length=6)

from rest_framework import serializers
from .models import User, SubscriptionPackage,Coupon,Discount,UserSubscription

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'mobile_number', 'otp', 'is_verified']

class SubscriptionPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPackage
        fields = '__all__'

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class UserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubscription
        fields = '__all__'

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class OTPVerificationSerializer(serializers.Serializer):
    mobile_number = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)
