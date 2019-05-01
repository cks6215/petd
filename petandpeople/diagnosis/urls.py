"""petandpeople URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


app_name = 'diagnosis'

urlpatterns = [
    path('', views.main, name='main'),
    path('main/<lang>', views.main_lang, name='main_lang'),

    path('diagnosis/me/<lang>', views.diagnosis_me, name='diagnosis_me'),
    path('diagnosis/pet/<lang>', views.diagnosis_pet, name='diagnosis_pet'),
    path('diagnosis/pet/<next_pet>/<lang>', views.check_pet, name='check_pet'),
    path('diagnosis/plan/<email>/<lang>', views.diagnosis_plan, name='diagnosis_plan'),
    path('diagnosis/photo_upload/<lang>', views.photo_upload, name='photo_upload'),
    path('diagnosis/check_email', views.check_email, name='check_email'),
    path('diagnosis/makeDiagnosis/<lang>', views.makeDiagnosis, name='makeDiagnosis'),
]
