from __future__ import annotations

import logging
from typing import Optional

from django.db import models
from django.conf import settings


class User_Group(models.Model):
    name = models.TextField(primary_key=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        managed = True
        db_table = "user_group"
