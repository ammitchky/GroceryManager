# Generated by Django 2.2.7 on 2019-11-10 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0004_auto_20191110_0327"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="location",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="item_locations.ItemLocation",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="item",
            name="specification",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="item_definitions.ItemSpecification",
            ),
            preserve_default=False,
        ),
    ]