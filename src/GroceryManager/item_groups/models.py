from __future__ import annotations

import logging
from typing import Optional

from django.db import models

from user_groups.models import User_Group


class Item_Group(models.Model):
    name = models.TextField(primary_key=True)
    user_group = models.ForeignKey(User_Group, on_delete=models.CASCADE, null=True)

    class Meta:
        managed = True
        db_table = "item_group"
