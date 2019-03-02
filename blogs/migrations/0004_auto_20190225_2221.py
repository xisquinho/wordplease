# Generated by Django 2.1.3 on 2019-02-25 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20190225_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(default='', upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
    ]
