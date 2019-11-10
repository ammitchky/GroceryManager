from __future__ import annotations

import logging
from typing import Optional

from django.conf import settings
from django.db import models


class Item_Definition(models.Model):
    name = models.TextField(primary_key=True)
    pantry_expiration = models.DurationField(null=True)
    fridge_expiration = models.DurationField(null=True)
    freezer_expiration = models.DurationField(null=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )

    class Meta:
        managed = True
        db_table = "item_definition"
