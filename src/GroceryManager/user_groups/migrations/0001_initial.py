# Generated by Django 2.2.7 on 2019-11-09 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Group',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'user_group',
                'managed': True,
            },
        ),
    ]