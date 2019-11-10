from django.contrib.auth.models import AbstractUser

class GroceryUser(AbstractUser):

    class Meta:
        managed = True
        db_table = "grocery_user"
