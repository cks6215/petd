# Generated by Django 2.2 on 2019-04-26 22:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0010_auto_20190426_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='diagnosis_pic',
            field=models.ImageField(default='static/pic_folder/None/no-img.jpg', upload_to='static/pic_folder'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 26, 22, 46, 10, 988585, tzinfo=utc), max_length=30),
        ),
    ]