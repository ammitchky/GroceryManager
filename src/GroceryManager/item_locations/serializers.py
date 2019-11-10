from rest_framework import serializers

from .models import ItemLocation


class ItemLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemLocation
        fields = "__all__"
