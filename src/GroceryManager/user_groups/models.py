from __future__ import annotations

import logging
from typing import Optional

from django.db import models


class User_Group(models.Model):
    name = models.TextField(primary_key=True)

    class Meta:
        managed = True
        db_table = "user_group"
