# Generated by Django 4.1.3 on 2022-12-03 23:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_data_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_post',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 3, 23, 3, 13, 983160, tzinfo=datetime.timezone.utc), verbose_name='Data postada'),
        ),
    ]
