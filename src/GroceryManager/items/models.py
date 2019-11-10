from __future__ import annotations

import logging
from typing import Optional

from django.conf import settings
from django.db import models

from grocery_user.models import GroceryUser
from item_definitions.models import ItemDefinition
from item_groups.models import ItemGroup
from item_locations.models import ItemLocation


class Item(models.Model):
    name = models.TextField(primary_key=True)
    static_item = models.ForeignKey(
        ItemDefinition, on_delete=models.DO_NOTHING, null=True
    )
    owner = models.ForeignKey(GroceryUser, on_delete=models.SET_NULL, null=True)
    item_location = models.ForeignKey(ItemLocation, on_delete=models.CASCADE, null=True)
    itemgroup = models.ManyToManyField(ItemGroup)
    expiration_date = models.DateTimeField(null=True)
    quantity = models.DecimalField(default=0.0, max_digits=7, decimal_places=2)
    desired_quantity = models.DecimalField(default=0.0, max_digits=7, decimal_places=2)

    class Meta:
        managed = True
        db_table = "item"
