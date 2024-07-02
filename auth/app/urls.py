from django.urls import path,include
from .views import (
    MobileLoginView, OTPVerificationView,
    SubscriptionPackageViewSet, CouponViewSet, 
    DiscountViewSet, UserSubscriptionViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'subscription-packages', SubscriptionPackageViewSet)
router.register(r'coupons', CouponViewSet)
router.register(r'discounts', DiscountViewSet)
router.register(r'user-subscriptions', UserSubscriptionViewSet)
urlpatterns = [
    path('login/', MobileLoginView.as_view(), name='mobile-login'),
    path('verify-otp/', OTPVerificationView.as_view(), name='otp-verification'),
    path('',include(router.urls))
    ]

