from django.contrib import admin
from .models import MyProfile, PetProfile, Diagnosis

# Register your models here.
admin.site.register(MyProfile)
admin.site.register(PetProfile)
admin.site.register(Diagnosis)