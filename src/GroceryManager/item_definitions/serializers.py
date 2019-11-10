from rest_framework import serializers

from .models import ItemDefinition, ItemSpecification


class ItemDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDefinition
        fields = "__all__"


class ItemSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSpecification
        fields = "__all__"
