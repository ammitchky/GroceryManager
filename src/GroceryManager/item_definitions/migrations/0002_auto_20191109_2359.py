# Generated by Django 2.2.7 on 2019-11-10 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item_definitions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemspecification',
            name='definition',
            field=models.ForeignKey(db_column='specification', on_delete=django.db.models.deletion.CASCADE, to='item_definitions.ItemDefinition'),
        ),
    ]
