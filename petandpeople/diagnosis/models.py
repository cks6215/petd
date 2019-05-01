import os

from django.conf import settings

from django.db import models
from django.utils import timezone

import datetime


# Create your models here.
class MyProfile(models.Model):
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=30, default='-')
    pet_num = models.IntegerField(default=0)
    zip = models.CharField(max_length=10, default='-')
    address = models.CharField(max_length=200, default='-')
    spending_time = models.CharField(max_length=30, default='0')

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

class PetProfile(models.Model):
    owner = models.ForeignKey(MyProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default='-')
    sex = models.CharField(max_length=10, default='he')
    age = models.IntegerField(default=0)
    age_unit = models.CharField(max_length=10, default='years')
    size = models.CharField(max_length=10, default='-')
    breed = models.CharField(max_length=30, default='-')
    spayed = models.CharField(max_length=10, default='-')
    weight = models.IntegerField(default=0)
    body_type = models.CharField(max_length=30, default='-')
    hair = models.CharField(max_length=10, default='-')
    ideal_weight = models.IntegerField(default=0)
    activity_level = models.CharField(max_length=20, default='active')
    eating_style = models.CharField(max_length=30, default='canBePicky')
    food_type = models.CharField(max_length=40, default='dry')
    food_brand = models.CharField(max_length=30, default='-')
    treats_amount = models.CharField(max_length=30, default='some')
    allergies = models.CharField(max_length=10, default='no')
    issues = models.CharField(max_length=50, default='no')

    def isAdultDog(self):
        if (self.age < 4) and (self.age_unit == "months"):
            return "유아기"
        elif ((self.age >= 4) and (self.age < 24) and (self.age_unit == "months")):
            return "청년기"
        elif ((self.age < 2) and (self.age_unit == "years")):
            return "청년기"
        elif (self.age >= 7) and (self.age_unit == "year"):
            return "노견"
        else:
            return "성견"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name




def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        dt = datetime.datetime.now()

        # get filename
        new_filename = '{}_{}.{}'.format(dt.date(), filename, ext)

        # return the whole path to the file
        return os.path.join(path, new_filename)
    return wrapper

class Diagnosis(models.Model):
    owner = models.ForeignKey(MyProfile, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=40, default='-')
    diagnosis_pic = models.FileField(null=True, blank=True, upload_to=path_and_rename('diagnosis_image'))
    pub_date = models.DateTimeField(max_length=30, default=timezone.now())


    # content = models.CharField(max_length=500, default='-')
    # features = models.CharField(max_length=100, default='-')

    def __str__(self):
        return self.pet_name

    def __unicode__(self):
        return self.pet_name


class DSample(models.Model):
    age = models.CharField(max_length=10, default='-')
    age_unit = models.CharField(max_length=10, default='-')
    weight = models.CharField(max_length=40, default='-')
    body_type = models.CharField(max_length=40, default='-')
    ideal_weight = models.CharField(max_length=40, default='-')
    activity_level = models.CharField(max_length=40, default='-')
    food_type = models.CharField(max_length=40, default='-')
    hair = models.CharField(max_length=40, default='-')
    size = models.CharField(max_length=40, default='-')
    allergies = models.CharField(max_length=10, default='no')
    issues = models.CharField(max_length=10, default='no')
    result = models.CharField(max_length=40, default='-')
