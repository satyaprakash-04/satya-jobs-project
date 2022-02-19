from django.contrib import admin
from sjobapp import models


class b_lurujobadmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone']


class bbsrjobadmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone']


class hydjobadmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone']


class punejobadmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligibility', 'address', 'email', 'phone']

# Register your models here.


admin.site.register(models.b_lurujobs, b_lurujobadmin)
admin.site.register(models.bbsrjobs, bbsrjobadmin)
admin.site.register(models.hydjobs, hydjobadmin)
admin.site.register(models.punejobs, punejobadmin)


