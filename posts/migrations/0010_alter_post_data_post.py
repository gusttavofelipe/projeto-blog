# Generated by Django 4.1.4 on 2022-12-19 14:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_post_data_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 14, 25, 27, 471338, tzinfo=datetime.timezone.utc), verbose_name='Data postada'),
        ),
    ]
