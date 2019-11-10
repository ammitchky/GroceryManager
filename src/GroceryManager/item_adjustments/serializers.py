from rest_framework import serializers

from .models import ItemAdjustment


class ItemAdjustmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAdjustment
        fields = "__all__"
