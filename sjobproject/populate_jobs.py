import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sjobproject.settings')

import django
django.setup()


from sjobapp.models import *
from random import *
from faker import Faker

fake = Faker()


def phonenogen():
    d1 = randint(6, 9)
    num = ''+str(d1)
    for i in range(9):
        num = num + str(randint(0,9))
    return int(num)


def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('project manager', 'Team leader', 'Software engineer'))
        feligibility = fake.random_element(elements=('b.Tech', 'M.Tech', 'MCA', 'PHD'))
        faddress = fake.address()
        fphoneno = phonenogen()
        femail = fake.email()
        hydjobs_record = hydjobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, address=faddress,email=femail, phone=fphoneno)
        b_lurujobs_record = b_lurujobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, address=faddress, email=femail,phone=fphoneno)
        bbsrjobs_record = bbsrjobs.objects.get_or_create(date=fdate, company=fcompany, title=ftitle, eligibility=feligibility, address=faddress, email =femail, phone=fphoneno)
        punejobs_record = punejobs.objects.get_or_create(date=fdate, company=fcompany,title=ftitle, eligibility=feligibility, address=faddress, email=femail, phone=fphoneno)
populate(5)
