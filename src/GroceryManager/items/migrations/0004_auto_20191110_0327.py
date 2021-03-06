# Generated by Django 2.2.7 on 2019-11-10 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("item_definitions", "0001_initial"),
        ("items", "0003_auto_20191110_0320"),
    ]

    operations = [
        migrations.RemoveField(model_name="item", name="static_item",),
        migrations.RemoveField(model_name="itemadjustment", name="item",),
        migrations.AddField(
            model_name="item",
            name="specification",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="item_definitions.ItemSpecification",
            ),
        ),
        migrations.AddField(
            model_name="itemadjustment",
            name="definition",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="item_definitions.ItemDefinition",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="itemadjustment",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="itemadjustment",
            name="user_group",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="user_groups.UserGroup",
            ),
            preserve_default=False,
        ),
    ]
