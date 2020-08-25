from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import viewsets
from farmeryyapp.models import Info
from farmeryyapp.serializers import InfoSerializer, UserSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django_otp.admin import OTPAdminSite
from .models import *



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
    return render(request,'trial.html')
def trialform(request):
    return render(request,'trialform.html')


def home(request):
    return render(request,'homedesign.html')

def about(request):
    return render(request,'about1.html')

def work(request):
    return render(request,'how_it_works.html')

def catalog(request):
    products = Product.objects.all()
    context= {'products':products}
    return render(request,'dairy.html', context)

def shop(request):
    product2 =Product2.objects.all()
    producttype=ProductType.objects.all()
    cate=Category1.objects.all()
    context= {'product2':product2,'producttype':producttype,'cate':cate}
    return render(request,'shop.html',context)

def team(request):
    team =Team.objects.all()
    context={'team':team}
    return render(request,'team.html',context)

def register(request):
    return render(request,'register.html')

def loginn(request):
    return render(request,'login.html')

def loginform(request):
    return render(request,'reg.html')


def reg(request):
    return render(request,'reg.html')

def myloginn(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
             messages.info(request,'invalid credentials')
             return redirect('mylogin')    
    else:
        return render(request,'mylogin.html')

class OTPAdmin(OTPAdminSite):
    pass