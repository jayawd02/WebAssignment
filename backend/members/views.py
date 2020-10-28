from django.http import HttpResponse
from .models import Member,MembershipPlan,Membership
from .serializers import  MemberSerializer,MembershipPlanSerializer,MembershipSerializer
from rest_framework import viewsets
from rest_framework import permissions


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MembershipPlanViewSet(viewsets.ModelViewSet):
    queryset = MembershipPlan.objects.all()
    serializer_class = MembershipPlanSerializer

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
