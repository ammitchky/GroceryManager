# Generated by Django 2.2.7 on 2019-11-10 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemadjustment",
            name="item",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="adjustments",
                to="item_definitions.ItemDefinition",
            ),
            preserve_default=False,
        ),
    ]
