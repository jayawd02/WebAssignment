from django.contrib import admin
from .models import Customer, MembershipPlan, Membership

admin.site.register(Customer)
admin.site.register(MembershipPlan)
admin.site.register(Membership)
