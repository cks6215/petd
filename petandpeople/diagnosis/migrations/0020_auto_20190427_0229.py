# Generated by Django 2.2 on 2019-04-27 02:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0019_auto_20190427_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='diagnosis_pic',
            field=models.FileField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 27, 2, 29, 34, 416855, tzinfo=utc), max_length=30),
        ),
    ]