# Generated by Django 4.1.4 on 2022-12-19 14:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0009_alter_comentario_data_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data_comentario',
            field=models.DateField(default=datetime.datetime(2022, 12, 19, 14, 29, 17, 53671, tzinfo=datetime.timezone.utc), verbose_name='Data'),
        ),
    ]
