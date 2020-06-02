# Generated by Django 3.0.2 on 2020-02-23 15:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authorization', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(upload_to='../uploads/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='registration_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 23, 15, 37, 15, 146691, tzinfo=utc)),
        ),
    ]
