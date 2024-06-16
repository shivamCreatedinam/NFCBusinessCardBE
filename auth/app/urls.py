from django.contrib import admin
from django.urls import path,include
from .views import MobileLoginView,OTPVerificationView
urlpatterns = [
    path('login/',MobileLoginView.as_view(),name='mobile_login'),
    path('verify-otp/',OTPVerificationView.as_view(),name='verify_otp'),
]
