import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTWo.settings')
#
import django
django.setup()
#
import random
from AppTwo.models import User
from faker import Faker
#
fakegen=Faker()

def generator():
    name=fakegen.name()
    nam=name.split()
    fn=nam[0]
    ln=nam[1]
    eml=fakegen.email()
    usr=User.objects.get_or_create(Fname=fn,Lname=ln,Email=eml)[0]
    usr.save()

def gen(N=10):
    for i in range(N):
        generator()


if __name__=="__main__":
    print("Populating Tables")
    gen()
    print("Population Complete")
