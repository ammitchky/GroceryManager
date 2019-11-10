from rest_framework import serializers

from .models import Item, ItemAdjustment
from item_groups.serializers import ItemGroupSerializer
from item_definitions.serializers import ItemSpecificationSerializer


class ItemAdjustmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAdjustment
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    adjustments = serializers.SerializerMethodField()
    item_group = ItemGroupSerializer(many=True, read_only=True)
    specification = ItemSpecificationSerializer(read_only=True)

    def get_adjustments(self, item):
        adjustments = ItemAdjustment.objects.filter(
            definition=item.specification.definition,
            user_group=item.location.user_group,
        )
        return ItemAdjustmentSerializer(list(adjustments), many=True).data

    class Meta:
        model = Item
        fields = "__all__"


class AdjustItemSerializer(serializers.Serializer):
    change = serializers.DecimalField(max_digits=7, decimal_places=2)
    price = serializers.DecimalField(required=False, max_digits=7, decimal_places=2)
    note = serializers.CharField(required=False, max_length=255)
