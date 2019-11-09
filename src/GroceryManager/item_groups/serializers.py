from rest_framework import serializers

from .models import Item_Group


class Item_GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Group
        fields = "__all__"
