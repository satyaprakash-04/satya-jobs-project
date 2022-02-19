from django.db import models

# Create your models here.


class b_lurujobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()


class bbsrjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()


class hydjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()


class punejobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    eligibility = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
