# Generated by Django 3.2.7 on 2021-09-16 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20210913_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='is_able',
            field=models.BooleanField(default=False),
        ),
    ]
