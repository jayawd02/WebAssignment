from django.contrib import admin
from .models import Customer, MembershipPlan

admin.site.register(Customer)
admin.site.register(MembershipPlan)