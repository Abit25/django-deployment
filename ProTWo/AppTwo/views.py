from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import UserProfileInfo
from AppTwo.forms import UserProfileForm,UserProfileInfoForm

# Create your views here.
def index(request):
    return render(request,"index2.html")



def register(request):

    registered=False
    if request.method=="POST" and registered==False:

        user_form=UserProfileForm(request.POST)
        userprof_form=UserProfileInfoForm(request.POST,request.FILES)

        if user_form.is_valid() and userprof_form.is_valid():

            user=user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            userprof=userprof_form.save(commit=False)
            userprof.user=user

            if 'profile_pic' in request.FILES:
                print('found it')
                userprof.profile_pic=request.FILES['profile_pic']
            else:
                print('No pic found')

            userprof.save()

            registered=True
            print("Completed")
        else:


            print(user_form.errors,userprof_form.errors)

    else:
        user_form=UserProfileForm()
        userprof_form=UserProfileInfoForm()

    return render(request,"register.html",{'user_form':user_form,'userprof_form':userprof_form,'registered':registered})
