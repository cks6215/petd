import json
import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import MyProfile, PetProfile, Diagnosis
# Create your views here.

def main(request):
    return render(request, 'diagnosis/main_kor.html')

def main_lang(request, lang):
    if lang == 'kor':
        return render(request, 'diagnosis/main_kor.html')

    elif lang == 'eng':
        return render(request, 'diagnosis/main.html')

    else:
        return render(request, 'diagnosis/main.html')


def diagnosis_me(request, lang):
    if lang == 'kor':
        return render(request, 'diagnosis/diagnosis_me_kor.html')

    elif lang == 'eng':
        return render(request, 'diagnosis/diagnosis_me.html')

    else:
        return render(request, 'diagnosis/diagnosis_me.html')


def diagnosis_pet(request, lang):
    if request.method == 'POST':
        tmp_email = request.POST.get('email')
        tmp_name = request.POST.get('name')
        tmp_pet_num = request.POST.get('pet_num')
        tmp_pet_name = request.POST.getlist('pet_name[]')
        tmp_zip = request.POST.get('zip')
        tmp_address = request.POST.get('address')
        tmp_spending_time = request.POST.get('spending_time')

        my_profile = None

        if MyProfile.objects.filter(email=tmp_email).exists():
            my_profile = MyProfile.objects.get(email=tmp_email)
            my_profile.name = tmp_name
            my_profile.pet_num = tmp_pet_num
            my_profile.zip = tmp_zip
            my_profile.address = tmp_address
            my_profile.spending_time = tmp_spending_time

            my_profile.save()

            tmp_pet = tmp_pet_name[0]

            pet_profile_query = PetProfile.objects.filter(owner=my_profile, name=tmp_pet)

            if pet_profile_query:
                context = {'email': tmp_email,
                           'name': tmp_name,
                           'pet_num': tmp_pet_num,
                           'pet_name':tmp_pet_name,
                           'zip': tmp_zip,
                           'spending_time': tmp_spending_time,
                           'p':tmp_pet,
                           'pet_profile':pet_profile_query[0],
                           }

                if lang == 'kor':
                    return render(request, 'diagnosis/diagnosis_pet_kor.html', context)

                elif lang == 'eng':
                    return render(request, 'diagnosis/diagnosis_pet_eng.html', context)

                else:
                    return render(request, 'diagnosis/diagnosis_pet_eng.html', context)

            else:
                context = {'email': tmp_email,
                           'name': tmp_name,
                           'pet_num': tmp_pet_num,
                           'pet_name': tmp_pet_name,
                           'zip': tmp_zip,
                           'spending_time': tmp_spending_time,
                           'p': tmp_pet,
                           }

                if lang == 'kor':
                    return render(request, 'diagnosis/diagnosis_pet_kor.html', context)

                elif lang == 'eng':
                    return render(request, 'diagnosis/diagnosis_pet_eng.html', context)

                else:
                    return render(request, 'diagnosis/diagnosis_pet_eng.html', context)

        else:
            MyProfile.objects.create(
                email = tmp_email,
                name = tmp_name,
                pet_num = tmp_pet_num,
                zip = tmp_zip,
                address = tmp_address,
                spending_time=tmp_spending_time
            )
            tmp_pet = tmp_pet_name[0]

            context = {'email': tmp_email,
                       'name': tmp_name,
                       'pet_num': tmp_pet_num,
                       'pet_name': tmp_pet_name,
                       'zip': tmp_zip,
                       'address': tmp_address,
                       'spending_time': tmp_spending_time,
                       'p': tmp_pet,
                       }

            if lang == 'kor':
                return render(request, 'diagnosis/diagnosis_pet_kor.html', context)

            elif lang == 'eng':
                return render(request, 'diagnosis/diagnosis_pet_eng.html', context)

            else:
                return render(request, 'diagnosis/diagnosis_pet_eng.html', context)

    else:
        if lang == 'kor':
            return render(request, 'diagnosis/diagnosis_pet_kor.html', context)

        elif lang == 'eng':
            return render(request, 'diagnosis/diagnosis_pet_eng.html', context)

        else:
            return render(request, 'diagnosis/diagnosis_pet_eng.html', context)


def check_pet(request, next_pet, lang):
    if request.method == 'POST':
        tmp_email = request.POST.get('email')
        tmp_name = request.POST.get('name')
        tmp_pet_num = request.POST.get('pet_num')
        tmp_pet_name = request.POST.getlist('pet_name[]')
        tmp_zip = request.POST.get('zip')
        tmp_address = request.POST.get('address')
        tmp_spending_time = request.POST.get('spending_time')
        tmp_this_pet_name = request.POST.get('this_pet_name')

        tmp_sex = request.POST.get('sex')
        tmp_age = request.POST.get('age')
        tmp_age_unit = request.POST.get('age_unit')
        tmp_size = request.POST.get('size')
        tmp_breed = request.POST.get('breed')
        tmp_spayed = request.POST.get('spayed')
        tmp_weight = request.POST.get('weight')
        tmp_body_type = request.POST.get('body_type')
        tmp_hair = request.POST.get('hair')
        tmp_ideal_weight = request.POST.get('ideal_weight')
        tmp_activity_level = request.POST.get('activity_level')
        tmp_eating_style = request.POST.get('eating_style')
        tmp_food_type = request.POST.get('food_type')
        tmp_food_brand = request.POST.get('food_brand')
        tmp_treats_amount = request.POST.get('treats_amount')
        tmp_allergies_check = request.POST.get('allergies_check')
        tmp_issues = request.POST.get('issues')

        my_profile = get_object_or_404(MyProfile, email=tmp_email)
        pet_profile = PetProfile.objects.filter(owner=my_profile, name=tmp_this_pet_name)

        if pet_profile:
            pet_profile.update(
                sex = tmp_sex,
                age = tmp_age,
                age_unit = tmp_age_unit,
                breed = tmp_breed,
                size = tmp_size,
                spayed = tmp_spayed,
                weight = tmp_weight,
                body_type = tmp_body_type,
                hair =tmp_hair,
                ideal_weight = tmp_ideal_weight,
                activity_level = tmp_activity_level,
                eating_style = tmp_eating_style,
                food_type = tmp_food_type,
                food_brand = tmp_food_brand,
                treats_amount = tmp_treats_amount,
                allergies = tmp_allergies_check,
                issues = tmp_issues,
            )
            if tmp_pet_name[-1] == tmp_this_pet_name:

                return redirect('diagnosis:diagnosis_plan', email=tmp_email, lang=lang)

            else:
                next_pet_profile = PetProfile.objects.filter(owner=my_profile, name=next_pet)


                if next_pet_profile:
                    context = {'email': tmp_email,
                               'name': tmp_name,
                               'pet_num': tmp_pet_num,
                               'pet_name': tmp_pet_name,
                               'zip': tmp_zip,
                               'spending_time': tmp_spending_time,
                               'p': next_pet,
                               'pet_profile':next_pet_profile[0],
                               }

                    if lang == 'kor':
                        return render(request, 'diagnosis/diagnosis_pet_kor.html', context)

                    elif lang == 'eng':
                        return render(request, 'diagnosis/diagnosis_pet_eng.html', context)

                    else:
                        return render(request, 'diagnosis/diagnosis_pet_eng.html', context)


                else:
                    context = {'email': tmp_email,
                               'name': tmp_name,
                               'pet_num': tmp_pet_num,
                               'pet_name': tmp_pet_name,
                               'zip': tmp_zip,
                               'spending_time': tmp_spending_time,
                               'p': next_pet,
                               }

                    if lang == 'kor':
                        return render(request, 'diagnosis/diagnosis_pet_kor.html', context)

                    elif lang == 'eng':
                        return render(request, 'diagnosis/diagnosis_pet_eng.html', context)

                    else:
                        return render(request, 'diagnosis/diagnosis_pet_eng.html', context)


        else:
            PetProfile.objects.create(
                owner = my_profile,
                name = tmp_this_pet_name,
                sex=tmp_sex,
                age=tmp_age,
                age_unit=tmp_age_unit,
                breed=tmp_breed,
                size=tmp_size,
                spayed=tmp_spayed,
                weight=tmp_weight,
                body_type=tmp_body_type,
                hair=tmp_hair,
                ideal_weight=tmp_ideal_weight,
                activity_level=tmp_activity_level,
                eating_style=tmp_eating_style,
                food_type=tmp_food_type,
                food_brand=tmp_food_brand,
                treats_amount=tmp_treats_amount,
                allergies=tmp_allergies_check,
                issues=tmp_issues,
            )

            if tmp_pet_name[-1] == tmp_this_pet_name:

                return redirect('diagnosis:diagnosis_plan', email=tmp_email, lang=lang)

            else:
                next_pet_profile = PetProfile.objects.filter(owner=my_profile, name=next_pet)

                if next_pet_profile:
                    context = {'email': tmp_email,
                               'name': tmp_name,
                               'pet_num': tmp_pet_num,
                               'pet_name': tmp_pet_name,
                               'zip': tmp_zip,
                               'spending_time': tmp_spending_time,
                               'p': next_pet,
                               'pet_profile': next_pet_profile[0],
                               }

                    if lang == 'kor':
                        return render(request, 'diagnosis/diagnosis_pet_kor.html', context)

                    elif lang == 'eng':
                        return render(request, 'diagnosis/diagnosis_pet_eng.html', context)

                    else:
                        return render(request, 'diagnosis/diagnosis_pet_eng.html', context)


                else:
                    context = {'email': tmp_email,
                               'name': tmp_name,
                               'pet_num': tmp_pet_num,
                               'pet_name': tmp_pet_name,
                               'zip': tmp_zip,
                               'spending_time': tmp_spending_time,
                               'p': next_pet,
                               }

                    if lang == 'kor':
                        return render(request, 'diagnosis/diagnosis_pet_kor.html', context)

                    elif lang == 'eng':
                        return render(request, 'diagnosis/diagnosis_pet_eng.html', context)

                    else:
                        return render(request, 'diagnosis/diagnosis_pet_eng.html', context)


    else:
        if lang == 'kor':
            return render(request, 'diagnosis/diagnosis_pet_kor.html', context)

        elif lang == 'eng':
            return render(request, 'diagnosis/diagnosis_pet_eng.html', context)

        else:
            return render(request, 'diagnosis/diagnosis_pet_eng.html', context)



def diagnosis_plan(request, email, lang):
    my_profile = get_object_or_404(MyProfile, email=email)
    pet_profiles = PetProfile.objects.filter(owner=my_profile)

    pet_profile_li = []
    for p in pet_profiles:

        #checking weakPoint
        weakness = []
        if (p.body_type == "rounded") or (p.body_type == "chunky"):
            weakness.append("fat")

        if (p.food_type == "dry") or (p.food_type == "dehydrated"):
            weakness.append("toothache")

        if (p.hair == "medium") or (p.hair == "long"):
            weakness.append("skin disease")


        if (p.size == "small"):
            if (p.isAdultDog == "노견") or (p.body_type == "chunky"):
                weakness.append("joint")

        elif (p.size == "middle"):
            if (p.isAdultDog== "노견") and (p.body_type == "rounded"):
                weakness.append("joint")

        elif (p.size == "big"):
            if (p.isAdultDog== "유아기") or (p.isAdultDog == "청년기"):
                weakness.append("joint")


        #calculate serving amount
        body_type_dict = {'skinny': '0', 'right': '1',
                          'rounded': '2', 'chunky': '3'}

        activity_level_dict = {'not': '0', 'normal': '1',
                               'very': '2', 'pro': '3'}

        tmp_serving = p.weight * 30 + 70
        if p.isAdultDog == "유아기":
            tmp_serving = tmp_serving * 3 * \
                          (-0.2 + 0.2 * body_type_dict[p.body_type]) * \
                          (-0.2 + 0.2 * activity_level_dict[p.activity_level])
        elif p.isAdultDog == "청년기":
            tmp_serving = tmp_serving * 2 * \
                          (-0.2 + 0.2 * body_type_dict[p.body_type]) * \
                          (-0.2 + 0.2 * activity_level_dict[p.activity_level])
        elif p.isAdultDog == "성견" or p.isAdultDog == "노견":
            tmp_serving = tmp_serving * \
                          (-0.2 + 0.2 * body_type_dict[p.body_type]) * \
                          (-0.2 + 0.2 * activity_level_dict[p.activity_level])

        # checking allergies
        if p.allergies== 'no':
            tmp_allergies = 0
        else:
            tmp_allergies = 1

        pet_profile_li.append([p, weakness, tmp_serving, tmp_allergies])


    context = {
        'email': email,
        'pet_profile_li':pet_profile_li,
    }

    if lang == 'kor':
        return render(request, 'diagnosis/diagnosis_plan_kor.html', context)

    elif lang == 'eng':
        return render(request, 'diagnosis/diagnosis_plan.html', context)

    else:
        return render(request, 'diagnosis/diagnosis_plan.html', context)


def photo_upload(request, lang):

    if lang == 'kor':
        return render(request, 'diagnosis/photo_upload_kor.html')

    elif lang == 'eng':
        return render(request, 'diagnosis/photo_upload.html')

    else:
        return render(request, 'diagnosis/photo_upload.html')


def check_email(request):
    tmp_email = request.GET['email']

    my_profile = MyProfile.objects.get(email=tmp_email)
    pet_profiles = PetProfile.objects.filter(owner=my_profile)
    if pet_profiles.exists():
        pet_name = []

        for pn in pet_profiles:
            pet_name.append(pn.name)

        return HttpResponse(json.dumps(pet_name), content_type='application/json')

    else:
        response = {'status': 'fail'}
        return HttpResponse(json.dump(response), content_type='application/json')


def makeDiagnosis(request, lang):
    if request.method == 'POST':
        tmp_email = request.POST.get('email')
        tmp_pet_name = request.POST.getlist('pet_name[]')
        tmp_owner = MyProfile.objects.get(email=tmp_email)

        for i in range(0, len(tmp_pet_name)):
            try:
                tmp_img = (request.FILES['diagnosis_img_'+tmp_pet_name[i]])

                Diagnosis.objects.create(
                    owner=tmp_owner,
                    pet_name=tmp_pet_name[i],
                    diagnosis_pic=tmp_img,
                )

            except:
                continue

        return redirect('diagnosis:main_lang', lang=lang)

    else:
        return redirect('diagnosis:main_lang', lang=lang)
