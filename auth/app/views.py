import random
from .models import User
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .serializers import OTPVerificationSerializer

class MobileLoginView(APIView):
    def post(self,request):
        mobile_number = request.data.get('mobile_number')
        if mobile_number:
            otp = str(random.randint(100000,999999))
            user,created = User.objects.get_or_create(mobile_number=mobile_number)
            user.otp = otp
            user.save()

            return Response({'message' : 'OTP sent successfully!', 'OTP' : otp},status=status.HTTP_200_OK)
        return Response({'error':'Mobile number is required'},status=status.HTTP_400_BAD_REQUEST)

class OTPVerificationView(APIView):
    def post(self,request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            mobile_number = serializer.validated_data['mobile_number']
            otp = serializer.validated_data['otp']
            try:
                user = User.objects.get(mobile_number=mobile_number,otp=otp)
                user.is_verified = True
                user.save()
                return Response({'message' : 'Mobile number verified successfully !'},status=status.HTTP_200_OK)
            except user.DoesNotExist:
                return Response({'error':'Invalid OTP or mobile number'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)