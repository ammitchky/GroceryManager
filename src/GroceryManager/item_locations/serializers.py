from rest_framework import serializers

from .models import Item_Location


class Item_LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Location
        fields = "__all__"
