from django.contrib import admin
from .models import User,Coupon,Discount,SubscriptionPackage,UserSubscription


admin.site.register(User)
admin.site.register(SubscriptionPackage)
admin.site.register(Discount)
admin.site.register(Coupon)
admin.site.register(UserSubscription)
