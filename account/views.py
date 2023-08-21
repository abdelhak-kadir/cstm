from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateUserForm ,OrderForm ,europForm,CarteForm
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime

# Create your views here.
def index(request):
    liste = news.objects.all().order_by('-published_date')
    first_three_items = liste[:3]

    trans_tube = video.objects.all()
    trans_num = trans_tube.count()
    paginator = Paginator(trans_tube,1) 
    page_number = request.GET.get('home')
    transporteur_page_obj = paginator.get_page(page_number)
    print(transporteur_page_obj)

    return render(request,"account/base.html",{'liste':first_three_items,'transporteur': transporteur_page_obj,'trans':trans_num,})  



def request(request):
     if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'اتصل بالرقم التالي لتأكيد طلبيتك')  # Success message
            return redirect('request')  # You can redirect to a success page after saving the order
        else:
            messages.error(request, 'يرجى تعبئة جميع الحقول')  # Error message for missing fields
     
     form = OrderForm()
     return render(request, 'account/request.html', {'form': form})

def create_carte(request):
    if request.method == 'POST':
        form = CarteForm(request.POST, request.FILES)
        cni = request.POST.get('cni')
        type_carte = request.POST.get('type_carte')
        formation_carte = request.POST.get('formation_carte')

        if carte.objects.filter(cni=cni).exists() and carte.objects.filter(formation_carte=formation_carte).exists() and carte.objects.filter(type_carte=type_carte).exists():
            messages.error(request, 'You\'re already signed.')  # Error message for duplicate submission
            return render(request,'cartes')
        else:
            if form.is_valid():
                form.save()
                messages.success(request, 'اتصل بالرقم التالي لتأكيد طلبيتك')  # Success message
                return redirect('carte')
            else:
                messages.error(request, 'يرجى تعبئة جميع الحقول')  # Error message for missing fields
    else:
        form = CarteForm()
    
    return render(request, 'account/carte.html', {'form': form})

def europ(request):
    if request.method == 'POST':
        form = europForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'اتصل بالرقم التالي لتأكيد طلبيتك')  # Success message
            return redirect('europ')
        else:
            messages.error(request, 'يرجى تعبئة جميع الحقول')  # Error message for missing fields
     
    form = europForm()
    return render(request, 'account/europ.html', {'form': form})
    
def signup(request):
    if request.method == 'POST':
       ice = request.POST.get('ice')
       if person.objects.filter(ICE=ice).exists() :
           messages.error(request, 'ICE already used or vide') 
       elif request.POST.get('name')=='' or  request.POST.get('prenom')==''  or  request.POST.get('ice')=='' or  request.POST.get('phone_number')==''  or  request.POST.get('encadrement')==''  or  request.POST.get('email')==''  or  request.POST.get('company')=='' or request.POST.get('weight')=='':
              messages.error(request, 'يرجى تعبئة جميع الحقول') 
       
       else:
            name = request.POST.get('name')
            prenom = request.POST.get('prenom')
            ice = request.POST.get('ice')
            email = request.POST.get('email')
            company=request.POST.get('company')
            encadrement = request.POST.get('encadrement')
            phone_number = request.POST.get('phone_number')
            weight = request.POST.get('weight')
            new_person = person(
                name=name,
                prenom=prenom,
                ICE=ice,
                company=company,
                encadrement=encadrement,
                email=email,
                phone_number=phone_number,
                weight=weight
            )
            new_person.save()
            messages.success(request,'اتصل بالرقم التالي لتأكيد تسجيلك ')
    return render(request, 'account/signup.html')

@login_required(login_url='admine')
def liste(request):
    liste = person.objects.all()
    liste1 = order.objects.all()
    liste2 = order_europ.objects.all()
    return render(request,"account/liste.html",{'transporteur':liste ,'transporteur1':liste1 , 'transporteur2':liste2 })

@login_required(login_url='admine')
def orders(request):
    liste = order.objects.all()
    return render(request,"account/order.html",{'transporteur':liste})

@login_required(login_url='admine')
def order_europe(request):
    liste = order_europ.objects.all()
    return render(request,"account/order_europe.html",{'transporteur':liste})

@login_required(login_url='admine')
def News(request):
    if request.method == 'POST':
       title= request.POST.get('title')
       description=request.POST.get('description')
       link=request.POST.get('link')
       
       new_news= news(
            title=title,
            description=description,
            link=link,   
        )
       new_news.save()
       messages.success(request,'تمت إضافة الخبر')

    context={}
    return render(request,"account/news.html")

@login_required(login_url='admine')
def tube(request):
    if request.method == 'POST':
       title= request.POST.get('title')
       link=request.POST.get('link')
       
       new_video= video(
            title=title,
            link=link,   
        )
       new_video.save()
       messages.success(request,'تمت إضافة الفيديو')

    return render(request,"account/youtube.html")

def navbar(request):
    liste = news.objects.all()
    first_three_items = liste[:3]
    return render(request,"account/base.html",{'liste':liste})   

@login_required(login_url='admine')
def registrePage(request):
    form =CreateUserForm()
    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()


    context={'form':form}
    return render(request,'account/registre.html',context)


def admine(request):
    if request.method == 'POST':
       username= request.POST.get('username')
       password=request.POST.get('password')
       user = authenticate(request , username=username , password=password)
       if user is not None :
           login(request,user)
           request.session.set_expiry(0)
           return redirect('dashboard')
       else:
           messages.info(request,'Username or password is incorrect')
           
    context={}
    return render(request,"account/admine.html",context)

@login_required(login_url='admine')
def logoutUser(request):
    logout(request)
    return redirect('admine')

@login_required(login_url='admine')
def dashboard(request):
    transporteur_list = person.objects.all().order_by('-published_date')
    transporteur1_list = order.objects.all().order_by('-published_date')
    transporteur2_list = order_europ.objects.all().order_by('-published_date')
    transporteur3_list = carte.objects.all().order_by('-published_date')

    trans_num = transporteur_list.count()
    trans_num1 = transporteur1_list.count()
    trans_num2 = transporteur2_list.count()
    trans_num3 = transporteur3_list.count()

    paginator = Paginator(transporteur_list,5) 
    page_number = request.GET.get('dashboard')
    transporteur_page_obj = paginator.get_page(page_number)

    paginator1 = Paginator(transporteur1_list, 5)  
    page_number1 = request.GET.get('dashboard')
    transporteur1_page_obj = paginator1.get_page(page_number1)

    paginator2 = Paginator(transporteur2_list, 5) 
    page_number2 = request.GET.get('dashboard')
    transporteur2_page_obj = paginator2.get_page(page_number2)

    paginator3 = Paginator(transporteur3_list, 5) 
    page_number3 = request.GET.get('dashboard')
    transporteur3_page_obj = paginator3.get_page(page_number3)


    return render(request, 'account/dashboard.html', {
        'transporteur': transporteur_page_obj,
        'transporteur1': transporteur1_page_obj,
        'transporteur2': transporteur2_page_obj,
        'transporteur3': transporteur3_page_obj,
        'trans':trans_num,
        'trans1':trans_num1,
        'trans2':trans_num2,
        'trans3':trans_num3,

    })
