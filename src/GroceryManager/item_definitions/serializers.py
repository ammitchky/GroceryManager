from rest_framework import serializers

from .models import ItemDefinition, ItemSpecification

class ItemSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSpecification
        fields = "__all__"


class ItemDefinitionSerializer(serializers.ModelSerializer):
    specifications = ItemSpecificationSerializer(many=True, read_only=True)
    class Meta:
        model = ItemDefinition
        fields = "__all__"
