from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateUserForm
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index(request):
    return render(request,"account/base.html")

def request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        prenom = request.POST.get('prenom')
        cni = request.POST.get('cni')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        weight = request.POST.get('weight')
        type_colis = request.POST.get('type_colis')
        from_colis = request.POST.get('from_colis')
        to_colis = request.POST.get('to_colis')

        new_order= order(
            name=name,
            prenom=prenom,
            cni=cni,
            email=email,
            phone_number=phone_number,
            weight=weight,
            type_colis=type_colis,
            from_colis=from_colis,
            to_colis=to_colis
        )

        new_order.save()
        messages.success(request,'اتصل بالرقم التالي لتأكيد طلبيتك ')
    return render(request, 'account/request.html')

def europ(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        prenom = request.POST.get('prenom')
        cni = request.POST.get('cni')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        weight = request.POST.get('weight')
        contry = request.POST.get('contry')
        type_colis = request.POST.get('type_colis')
        from_colis = request.POST.get('from_colis')
        to_colis = request.POST.get('to_colis')

        new_order= order_europ(
            name=name,
            prenom=prenom,
            cni=cni,
            email=email,
            phone_number=phone_number,
            weight=weight,
            contry=contry,
            type_colis=type_colis,
            from_colis=from_colis,
            to_colis=to_colis
        )

        new_order.save()
        messages.success(request,'اتصل بالرقم التالي لتأكيد طلبيتك ')
    return render(request,"account/europ.html")

def signup(request):
    if request.method == 'POST':
       name= request.POST.get('name')
       prenom=request.POST.get('prenom')
       user = authenticate(request , name=name , prenom=prenom)
       if user is not None :
           messages.info(request,' طلبيتك ')
       else:
            name = request.POST.get('name')
            prenom = request.POST.get('prenom')
            nickname = request.POST.get('nickname')
            cni = request.POST.get('cni')
            birth_date = request.POST.get('birth_date')
            gender = request.POST.get('gender')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            weight = request.POST.get('weight')
            new_person = person(
                name=name,
                prenom=prenom,
                nickname=nickname,
                cni=cni,
                birth_date=birth_date,
                gender=gender,
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

def news(request):
    return render(request,"account/news.html")

def navbar(request):
    liste = news.objects.all().order_by('published_date')
    first_three_items = liste[:3]
    return render(request,"account/base.html",{'liste':first_three_items})   

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
           return redirect('dashboard')
       else:
           messages.info(request,'Username or password is incorrect')
           
    context={}
    return render(request,"account/admine.html",context)

def logoutUser(request):
    logout(request)
    return redirect('admine')

@login_required(login_url='admine')
def dashboard(request):
    transporteur_list = person.objects.all().order_by('-published_date')
    transporteur1_list = order.objects.all().order_by('published_date')
    transporteur2_list = order_europ.objects.all().order_by('published_date')
    
    trans_num = transporteur_list.count()
    trans_num1 = transporteur1_list.count()
    trans_num2 = transporteur2_list.count()

    paginator = Paginator(transporteur_list,5) 
    page_number = request.GET.get('dashboard')
    transporteur_page_obj = paginator.get_page(page_number)

    paginator1 = Paginator(transporteur1_list, 5)  
    page_number1 = request.GET.get('dashboard')
    transporteur1_page_obj = paginator1.get_page(page_number1)

    paginator2 = Paginator(transporteur2_list, 5) 
    page_number2 = request.GET.get('dashboard')
    transporteur2_page_obj = paginator2.get_page(page_number2)

    return render(request, 'account/dashboard.html', {
        'transporteur': transporteur_page_obj,
        'transporteur1': transporteur1_page_obj,
        'transporteur2': transporteur2_page_obj,
        'trans':trans_num,
        'trans1':trans_num1,
        'trans2':trans_num2,

    })
