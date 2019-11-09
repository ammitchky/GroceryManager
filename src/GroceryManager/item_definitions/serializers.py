from rest_framework import serializers

from .models import Item_Definition


class Item_DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Definition
        fields = "__all__"
