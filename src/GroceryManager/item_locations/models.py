from __future__ import annotations

import logging
from typing import Optional

from django.db import models

from user_groups.models import UserGroup

STORAGE_LOCATION_CHOICE = [
    ("pantry", "Pantry"),
    ("fridge", "Fridge"),
    ("freezer", "Freezer"),
    ("cart", "Cart"),
]


class ItemLocation(models.Model):
    name = models.TextField(primary_key=True)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, null=True)
    location_type = models.TextField(choices=STORAGE_LOCATION_CHOICE, null=True)

    class Meta:
        managed = True
        db_table = "item_location"
