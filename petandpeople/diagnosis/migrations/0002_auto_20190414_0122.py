# Generated by Django 2.2 on 2019-04-14 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diagnosis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('name', models.CharField(max_length=30)),
                ('pet_num', models.IntegerField(default=0)),
                ('zipcode', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('spending_time', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='statusofpet',
            name='pet_num',
        ),
        migrations.RemoveField(
            model_name='statusofpet',
            name='spending_time',
        ),
        migrations.RemoveField(
            model_name='statusofpet',
            name='username',
        ),
        migrations.AddField(
            model_name='statusofpet',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='diagnosis.MyProfile'),
            preserve_default=False,
        ),
    ]
