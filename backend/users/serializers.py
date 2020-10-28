from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.first_name')

    class Meta:
        model = Profile
        fields = ['id','user','profile_pic']