import random
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status, permissions,viewsets
from .models import User,SubscriptionPackage,Coupon,Discount,UserSubscription
from .serializers import (UserSerializer,SubscriptionPackageSerializer,CouponSerializer,DiscountSerializer,UserSubscriptionSerializer,OTPVerificationSerializer)
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

class MobileLoginView(APIView):
    def post(self, request):
        mobile_number = request.data.get('mobile_number')
        if mobile_number:
            otp = str(random.randint(100000, 999999))
            user, created = User.objects.get_or_create(mobile_number=mobile_number)
            user.otp = otp
            user.save()

            #Here u would send the OTP vis SMS. Fornow, we return it in the response.
            return Response({'message': 'OTP sent successfully!', 'OTP': otp}, status=status.HTTP_200_OK)
        return Response({'error': 'Mobile number is required'}, status=status.HTTP_400_BAD_REQUEST)

class OTPVerificationView(APIView):
    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            mobile_number = serializer.validated_data['mobile_number']
            otp = serializer.validated_data['otp']
            try:
                user = User.objects.get(mobile_number=mobile_number, otp=otp)
                user.is_verified = True
                user.save()
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh':str(refresh),
                    'access':str(refresh.access_token),
                    'message': 'Mobile number verified successfully!',
                },status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': 'Invalid OTP or mobile number'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubscriptionPackageViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionPackage.objects.all()
    serializer_class = SubscriptionPackageSerializer

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
class UserSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user_id = data.get('user')

        # Handle case where user does not exist
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValidationError({'user': 'User with this ID does not exist.'})

        # Handle case where package does not exist
        try:
            package = SubscriptionPackage.objects.get(id=data['package'])
        except SubscriptionPackage.DoesNotExist:
            raise ValidationError({'package': 'SubscriptionPackage with this ID does not exist.'})
        
        # Handle case where coupon does not exist
        coupon_code = data.get('coupon')
        coupon = None
        if coupon_code:
            coupon = Coupon.objects.filter(code=coupon_code).first()
            if not coupon:
                raise ValidationError({'coupon': 'Coupon with this code does not exist.'})
        
        # Calculate total price
        base_price = package.price
        total_discount = 0
        
        if coupon and coupon.expiration_date >= timezone.now().date():
            total_discount += coupon.discount_percentage

        # Apply active discounts
        active_discounts = Discount.objects.filter(is_active=True)
        for discount in active_discounts:
            total_discount += discount.discount_percentage

        total_price = base_price - (base_price * (total_discount / 100))
        
        # Create UserSubscription
        user_subscription = UserSubscription.objects.create(
            user=user,
            package=package,
            start_date=timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=package.duration_days),
            coupon=coupon,
            total_price=total_price,
            status=data.get('status', 'active')
        )

        serializer = self.get_serializer(user_subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

