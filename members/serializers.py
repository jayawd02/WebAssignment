from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Member,Membership,MembershipPlan

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields =['id','user','first_name','last_name','gender','date_of_birth','height','address_line1','address_line2','email','contact_no1','contact_no2','health_problems','allergies','meal_preference']


class MembershipPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = MembershipPlan
        exclude = ['status']

class MembershipSerializer (serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = ['id','membership_plan','members','start_date','end_date','discount','final_fee']


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email']