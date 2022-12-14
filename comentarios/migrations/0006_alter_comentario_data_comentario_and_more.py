# Generated by Django 4.1.3 on 2022-12-03 23:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_data_post'),
        ('comentarios', '0005_alter_comentario_data_comentario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='data_comentario',
            field=models.DateField(default=datetime.datetime(2022, 12, 3, 23, 17, 9, 384650, tzinfo=datetime.timezone.utc), verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='post_comentario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post', verbose_name='Post'),
        ),
    ]
