# Generated by Django 2.2.7 on 2019-11-10 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item_definitions', '0002_auto_20191109_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemspecification',
            name='definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='item_definitions.ItemDefinition'),
        ),
    ]
