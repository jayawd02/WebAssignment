from django.contrib import admin
from .models import Member, MembershipPlan, Membership

class MemberAdmin(admin.ModelAdmin):
    fields =['user','first_name','last_name','gender','date_of_birth','height','address_line1','address_line2','email','contact_no1','contact_no2','health_problems','allergies','meal_preference','photo']
    list_display=('first_name','last_name','email','user')
    list_filter = ['user']
    search_fields = ['user']

class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name','plan_type','duration','fee','status')
    list_filter = ['status','duration']
    search_fields = ['duration']

class MembershipAdmin(admin.ModelAdmin):
    list_display = ('membership_plan','start_date','end_date')
    list_filter = ['membership_plan']
    search_fields =['membership_plan']



admin.site.register(Member,MemberAdmin)
admin.site.register(MembershipPlan,MembershipPlanAdmin)
admin.site.register(Membership,MembershipAdmin)
