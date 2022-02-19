from django.shortcuts import render
from sjobapp import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.


def jobhome(request):
    return render(request, 'sjobapp/home.html')


def bbsrjobinfo(request):
    bbsrjob_list = models.bbsrjobs.objects.order_by('-date')
    paginator = Paginator(bbsrjob_list, 5)
    page_number = request.GET.get('page')
    try:
        bbsrjob_list = paginator.page(page_number)
    except PageNotAnInteger:
        bbsrjob_list = paginator.page(1)
    except EmptyPage:
        bbsrjob_list = paginator.page(paginator.num_pages)
    my_dict = {'bbsrjob_list':bbsrjob_list}
    return render(request, 'sjobapp/bbsrjobs.html', context=my_dict)


def hydjobinfo(request):
    hydjob_list = models.hydjobs.objects.order_by('date')
    my_dict = {'hydjob_list': hydjob_list}
    return render(request, 'sjobapp/hydjobs.html', context=my_dict)


def b_lurujobiinfo(request):
    b_lurujob_list = models.b_lurujobs.objects.order_by('date')
    my_dict = {'b_lurujob_list': b_lurujob_list}
    return render(request, 'sjobapp/b_lurujobs.html', context=my_dict)


def punejobinfo(request):
    punejob_list = models.punejobs.objects.order_by('date')
    my_dict = {'punejob_list': punejob_list}
    return render(request, 'sjobapp/punejobs.html', context=my_dict)
