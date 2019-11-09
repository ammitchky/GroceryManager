from rest_framework import serializers

from .models import User_Group


class User_GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Group
        fields = "__all__"
