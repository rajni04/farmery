from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from farmeryyapp.models import Info,Product
from farmeryyapp.serializers import InfoSerializer, UserSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django_otp.admin import OTPAdminSite
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
from math import ceil
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger



class InfoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication] 
    permission_classes=[IsAuthenticated]
    def list(self,request):   
        user=request.user
        print("user", user)
        info=Info.objects.all()
        serializer=InfoSerializer(info,many=True,context={"request":request})
        response_dict={"error":False,"message":"All User List Data","data":serializer.data}
        return JsonResponse(response_dict)

    def create(self,request):
            serializer=InfoSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"User Data Save Successfully"}
    
            return JsonResponse(dict_response)
info_list=InfoViewSet.as_view({"get":"list"})
info_create=InfoViewSet.as_view({"post":"create"})




def index(request):
    return render(request,'home.html')

def trial(request):
    return render(request,'productdetail.html')
def trialform(request):
    return render(request,'trialform.html')


def home(request):
    content=Circl.objects.all()[:2]
    sliderhome=Sliderhome.objects.all()
    offpro=Offerproduct.objects.all()
    offpro_page = Paginator(offpro,4)# Show 25 contacts per page.
    page = request.GET.get('page')
    try:
        # create Page object for the given page
        page_objj = offpro_page.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        page_objj = offpro_page.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        page_objj= offpro_page.page(offpro_page.num_pages)
   
   # n=len(offpro)
    #nSlides=n//4+ ceil((n/4)-(n//4))
    #allProds=[[ offpro, range(1, len(offpro)), nSlides],[offpro, range(1, len(offpro)), nSlides]]
   # params={'allProds':allProds }

    aboutdata=Homedata.objects.all().order_by('-id')[:1]   #last data
    return render(request,'homedesign.html',{'sliderhome':sliderhome,'content':content,'aboutdata':aboutdata,'offpro': offpro,'page_objj': page_objj})
    #return render(request,'NewDesign/home.html')

def home1(request):
    #return render(request,'homedesign.html')
    return render(request,'NewDesign/home.html')

def about(request):
    return render(request,'about1.html')

def work(request):
    work=Work.objects.all().distinct('workdesc')
    context= {'work':work}
    return render(request,'how_it_works.html',context)

def catalog(request):
    products = Product.objects.all()
    context= {'products':products}
    return render(request,'dairy.html', context)

def shop(request):
    product2 =Product2.objects.all()
    producttype=ProductType.objects.all()
    cate=Category1.objects.all()
    context= {'product2':product2,'producttype':producttype,'cate':cate}
    return render(request,'fruitngroc.html',context)

def teamHome(request):
    team =Team.objects.all()
    context={'team':team}
    return render(request,'team1.html',context)


def blog(request):
    #team =Team.objects.all()
   # context={'team':team}
    return render(request,'blog.html')

def register(request):
    return render(request,'register.html')

def loginn(request):
    return render(request,'login.html')

def loginform(request):
    return render(request,'reg.html')


def reg(request):
    return render(request,'reg.html')

"""def myloginn(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("admin")
        else:
             messages.info(request,'invalid credentials')
             return redirect('mylogin')    
    else:
        return render(request,'mylogin.html')"""

def homeadmin_template(request):
   
    return render(request,'Admin/homeadmin_template.html')

def product(request):
   
    return render(request,'Admin/product.html')

def viewproduct(request):
    product=Product.objects.all()
    return render(request,"Admin/table.html",{'product': product})

def viewFruitGrocery(request):
    product2=Product2.objects.all()
    return render(request,"Admin/ViewFruitGrocery.html",{'product2': product2})



def delete_product(request,product_id):
   product=Product.objects.get(id=product_id)
   product.delete()
   return redirect("/viewproduct")


class OTPAdmin(OTPAdminSite):
    pass

def myloginn(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            if user.user_type =="1":
                 return redirect('Admin/homeadmin_template')
            
            elif user.user_type =="2":
                 return redirect('customer_home')
        else:
             messages.error(request,"Invalid Login Details")
             return redirect('mylogin1.html')    
    else:
        return render(request,'mylogin1.html')      


def loogout(request):
    logout(request)
    return HttpResponseRedirect("/")

     

def catalog(request):
    products = Product.objects.all()
    context= {'products':products}
    return render(request,'dairy.html', context)


