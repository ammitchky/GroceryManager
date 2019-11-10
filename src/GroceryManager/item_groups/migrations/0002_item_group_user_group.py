# Generated by Django 2.2.7 on 2019-11-10 03:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_groups", "0002_user_group_user"),
        ("item_groups", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item_group",
            name="user_group",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user_groups.User_Group",
            ),
        ),
    ]
