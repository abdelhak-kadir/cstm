from django.shortcuts import redirect , render
from App.models import *

def BASE(request):
    return render(request,'base1.html')

def HOME(request):
    category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status = 'PUBLISH').order_by('-id')

    context = {
        'category' : category,
        'course': course,
    }
    return render(request,'Main/home.html',context)

def SINGLE_COURSE(request):
    return render(request,'Main/single_course.html')


def CONTACT_US(request):
    return render(request,'Main/contact_us.html')

def ABOUT_US(request):
    return render(request,'Main/about_us.html')