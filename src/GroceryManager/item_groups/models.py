from __future__ import annotations

import logging
from typing import Optional

from django.db import models


class Item_Group(models.Model):
    name = models.TextField(primary_key=True)

    class Meta:
        managed = True
        db_table = "item_group"
