from __future__ import annotations

import logging
from typing import Optional

from django.db import models

from item_definitions.models import ItemDefinition
from user_groups.models import UserGroup


class ItemAdjustment(models.Model):
    name = models.TextField()
    item_type = models.ForeignKey(ItemDefinition, on_delete=models.CASCADE, null=True)
    user_group = models.ForeignKey(UserGroup, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = "item_adjustment"
