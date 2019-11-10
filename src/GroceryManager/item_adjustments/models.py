from __future__ import annotations

import logging
from typing import Optional

from django.db import models

from item_definitions.models import ItemDefinition
from user_groups.models import UserGroup


class ItemAdjustment(models.Model):
    item_type = models.ForeignKey(ItemDefinition, on_delete=models.CASCADE, null=True)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, null=True)
    quantity = models.DecimalField(default=0.0, max_digits=7, decimal_places=2)
    cost = models.DecimalField(decimal_places=2, default=0.0, max_digits=7)
    note = models.TextField(null=True)

    class Meta:
        managed = True
        db_table = "item_adjustment"
