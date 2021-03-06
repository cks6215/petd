# Generated by Django 2.2 on 2019-04-26 22:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0007_diagnosis_diagnosisimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diagnosisimage',
            old_name='reservation',
            new_name='diagnosis',
        ),
        migrations.RemoveField(
            model_name='diagnosisimage',
            name='pet_name',
        ),
        migrations.AddField(
            model_name='diagnosisimage',
            name='diagnosis_pic',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 26, 22, 23, 24, 157495, tzinfo=utc), max_length=30),
        ),
    ]
