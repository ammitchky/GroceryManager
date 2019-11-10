from __future__ import annotations

import logging
from typing import Optional

from django.conf import settings
from django.db import models

from item_definitions.models import Item_Definition
from item_groups.models import Item_Group
from item_locations.models import Item_Location


class Item(models.Model):
    name = models.TextField(primary_key=True)
    static_item = models.ForeignKey(
        Item_Definition, on_delete=models.DO_NOTHING, null=True
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    item_location = models.ForeignKey(
        Item_Location, on_delete=models.CASCADE, null=True
    )
    itemgroup = models.ManyToManyField(Item_Group)
    expiration_date = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = "item"
