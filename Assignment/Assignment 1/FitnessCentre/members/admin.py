from django.contrib import admin
from .models import Member, MembershipPlan, Membership

admin.site.register(Member)
admin.site.register(MembershipPlan)
admin.site.register(Membership)
