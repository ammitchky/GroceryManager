from __future__ import annotations

import logging
from typing import Optional

from django.db import models
from item_definitions.models import Item_Definition
from user_groups.models import User_Group


class Item_Adjustment(models.Model):
    name = models.TextField(primary_key=True)
    item_type = models.ForeignKey(Item_Definition, on_delete=models.CASCADE, null=True)
    user_group = models.ForeignKey(User_Group, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = "item_adjustment"
