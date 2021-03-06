# Generated by Django 2.2 on 2019-04-26 23:22

import datetime
import django.core.files.storage
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0015_auto_20190426_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='diagnosis_pic',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(base_url='/static/', location='/static'), upload_to='diagnosis'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 26, 23, 22, 24, 88753, tzinfo=utc), max_length=30),
        ),
    ]
