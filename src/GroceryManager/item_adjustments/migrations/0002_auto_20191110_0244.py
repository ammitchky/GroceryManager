# Generated by Django 2.2.7 on 2019-11-10 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_adjustments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemadjustment',
            name='name',
        ),
        migrations.AddField(
            model_name='itemadjustment',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
        migrations.AddField(
            model_name='itemadjustment',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='itemadjustment',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]