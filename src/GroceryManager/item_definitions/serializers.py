from rest_framework import serializers

from .models import ItemDefinition, ItemSpecification


class PartialItemSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSpecification
        fields = "__all__"


class ItemDefinitionSerializer(serializers.ModelSerializer):
    specifications = PartialItemSpecificationSerializer(many=True, read_only=True)

    class Meta:
        model = ItemDefinition
        fields = "__all__"


class ItemSpecificationSerializer(serializers.ModelSerializer):
    definition = ItemDefinitionSerializer(read_only=True)

    class Meta:
        model = ItemSpecification
        fields = "__all__"
