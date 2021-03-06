from __future__ import annotations

import logging
from typing import Optional

from django.conf import settings
from django.db import models

from grocery_user.models import GroceryUser


class UserGroup(models.Model):
    name = models.CharField(max_length=255)
    user = models.ManyToManyField(GroceryUser)

    class Meta:
        managed = True
        db_table = "user_group"
