from __future__ import annotations

import logging
from typing import Optional

from django.conf import settings
from django.db import models

from grocery_user.models import GroceryUser
from item_definitions.models import ItemDefinition, ItemSpecification
from item_groups.models import ItemGroup
from item_locations.models import ItemLocation
from user_groups.models import UserGroup


class ItemAdjustment(models.Model):
    definition = models.ForeignKey(ItemDefinition, on_delete=models.CASCADE)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(GroceryUser, on_delete=models.SET_NULL, null=True)
    quantity = models.DecimalField(default=0.0, max_digits=7, decimal_places=2)
    cost = models.DecimalField(decimal_places=2, default=0.0, max_digits=7)
    note = models.TextField(null=True)

    class Meta:
        managed = True
        db_table = "item_adjustment"


class Item(models.Model):
    name = models.CharField(max_length=255)
    specification = models.ForeignKey(ItemSpecification, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(GroceryUser, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(ItemLocation, on_delete=models.CASCADE)
    item_group = models.ManyToManyField(ItemGroup, blank=True)
    expiration_date = models.DateTimeField(null=True)
    quantity = models.DecimalField(default=0.0, max_digits=7, decimal_places=2)
    desired_quantity = models.DecimalField(default=0.0, max_digits=7, decimal_places=2)

    class Meta:
        managed = True
        db_table = "item"
