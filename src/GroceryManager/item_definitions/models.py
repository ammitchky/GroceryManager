from __future__ import annotations

import logging
from typing import Optional

from django.conf import settings
from django.db import models

from grocery_user.models import GroceryUser


class ItemDefinition(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(GroceryUser, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = "item_definition"


class ItemSpecification(models.Model):
    name = models.CharField(max_length=255)
    definition = models.ForeignKey(
        ItemDefinition, on_delete=models.CASCADE, related_name="specifications"
    )
    pantry_expiration = models.DurationField(null=True)
    fridge_expiration = models.DurationField(null=True)
    freezer_expiration = models.DurationField(null=True)
    created_by = models.ForeignKey(GroceryUser, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = "item_specification"
