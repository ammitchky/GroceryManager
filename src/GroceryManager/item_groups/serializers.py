from rest_framework import serializers

from .models import ItemGroup


class ItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemGroup
        fields = "__all__"
