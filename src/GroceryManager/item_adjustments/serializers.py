from rest_framework import serializers

from .models import Item_Adjustment


class Item_AdjustmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Adjustment
        fields = "__all__"
