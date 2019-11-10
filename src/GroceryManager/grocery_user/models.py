from django.conf import settings
from django.db import models


class GroceryUser(models.Model):
    auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = "grocery_user"
