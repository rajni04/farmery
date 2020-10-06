from django.shortcuts import render
from rest_framework import viewsets ,generics
from farmeryyapp.serializers import InfoSerializer, UserSerializer,ProductSerializer,Category1Serializer,ProductTypeSerializer,Product2Serializer,RatingSerializer
from farmeryyapp.models import Info,Product,Category1,ProductType,Product2,Rating
from rest_framework.response import Response
from rest_framework import status
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from django.contrib.auth import login as django_login
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

"""class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer"""

# Create your views here.

"""class InfoViewSet(viewsets.ModelViewSet):    
    permission_classes=[TokenAuthentication]
    authentication_classes=[IsAuthenticated]       ------------- its working  ------------                                      
    def list(request):
        if request.method=='GET':
            info=Info.objects.all()
            serializer=InfoSerializer(info,many=True)
            return JsonResponse(serializer.data,safe=False)

        elif request.method == 'POST':
            data=JSONParser().parse(request)
            serializer=InfoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            return JsonResponse(serializer.errors,status=400)"""

class InfoViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication] 
    permission_classes=[IsAuthenticated]
    
    def list(self,request):  
        user=request.user
        print("user is",user)
        info=Info.objects.all()
        serializer=InfoSerializer(info,many=True,context={"request":request})
        response_dict={"error":False,"message":"All User List Data","data":serializer.data}
        return Response(response_dict)

    def create(self,request):
            user=request.user
            print("user is",user)
            serializer=InfoSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"User Data Save Successfully"}
    
            return Response(dict_response)


    def update(self,request,pk=None):
        try:
            queryset=Info.objects.all()
            info=get_object_or_404(queryset,pk=pk)
            serializer=InfoSerializer(info,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated  Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating C Data"}

        return Response(dict_response)

    def retrieve(self,request,pk=None):
        queryset=Info.objects.all()
        info=get_object_or_404(queryset,pk=pk)
        serializer=InfoSerializer(info,context={"request":request})
        return Response({"error":False,"message":"Single Data Fetch","data":serializer.data})
user_list=InfoViewSet.as_view({"get":"list"})
user_create=InfoViewSet.as_view({"post":"create"})


class LoginViewSet(viewsets.ViewSet):
    serializer_class= AuthTokenSerializer
    def create(self,request):
        return ObtainAuthToken().post(request)




class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication] 
    permission_classes=[IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
  #  template_name = 'trial.html'
    def list(self,request):  
        product=Product.objects.all()
        serializer=ProductSerializer(product,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Product List Data","data":serializer.data}
        return render(request,"Admin/ViewProduct.html",response_dict)
    

    def create(self,request):
        try:
           
            serializer=ProductSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            product_id=serializer.data['id'];
            print(product_id,"ttttttttttt")
            dict_response={"error":False,"message":"User Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Data"}
        return Response(request,"Admin/Product.html",dict_response)

    def update(self,request,pk=None):
        try:
            queryset=Product.objects.all()
            product=get_object_or_404(queryset,pk=pk)
            serializer=ProductSerializer(product,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated  Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating C Data"}

        return Response(request,"Admin/EditProduct.html",dict_response)
  
    def retrieve(self,request,pk=None):
        queryset=Product.objects.all()
        product=get_object_or_404(queryset,pk=pk)
        serializer=ProductSerializer(product,context={"request":request})
        return Response({"error":False,"message":"Single Data Fetch","data":serializer.data})


product_list=ProductViewSet.as_view({"get":"list"})
product_create=ProductViewSet.as_view({"post":"create"})
product_update=ProductViewSet.as_view({"put":"update"})


class Category1ViewSet(viewsets.ModelViewSet):
    def list(self,request):  

        category=Category1.objects.all()
        serializer=Category1Serializer(category,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Category List Data","data":serializer.data}
        return Response(response_dict)
        print(response_dict)

    def create(self,request):
        try:
           
            serializer=Category1Serializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            category_id=serializer.data['id'];
            print(category_id,"view the category after post method")
            category_details_list=[]
            for category_detail in request.data["category_details"]:
                print(category_detail)
                #Adding medicine id which will work for medicine details serializer
                #medicine_detail["medicine_id"]=medicine_id
                #medicine_details_list.append(medicine_detail)
               # print(medicine_detail)

           # serializer2=MedicalDetailsSerializer(data=medicine_details_list,many=True,context={"request":request})
           # serializer2.is_valid()
           # serializer2.save()


            dict_response={"error":False,"message":"category Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"category During Saving Data"}
        return Response(dict_response)

    def update(self,request,pk=None):
        try:
            queryset=Category1.objects.all()
            category=get_object_or_404(queryset,pk=pk)
            serializer=Category1Serializer(category,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Category Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Category Data"}

        return Response(dict_response)

    def retrieve(self,request,pk=None):
        queryset=Category1.objects.all()
        category=get_object_or_404(queryset,pk=pk)
        serializer=Category1Serializer(category,context={"request":request})
        return Response({"error":False,"message":"Single Data Fetch","data":serializer.data})


category_list=Category1ViewSet.as_view({"get":"list"})
category_create=Category1ViewSet.as_view({"post":"create"})
category_update=Category1ViewSet.as_view({"put":"update"})



class ProductTypeViewSet(viewsets.ModelViewSet):
    def list(self,request):  

        producttype=ProductType.objects.all()
        serializer=ProductTypeSerializer(producttype,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Product List Data","data":serializer.data}
        return Response(response_dict)
        print(response_dict)

    def create(self,request):
        try:
           
            serializer=ProductTypeSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"category Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"category During Saving Data"}
        return Response(dict_response)

    def update(self,request,pk=None):
        try:
            queryset=ProductType.objects.all()
            producttype=get_object_or_404(queryset,pk=pk)
            serializer=ProductTypeSerializer(producttype,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Category Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Category Data"}

        return Response(dict_response)

    def retrieve(self,request,pk=None):
        queryset=ProductType.objects.all()
        producttype=get_object_or_404(queryset,pk=pk)
        serializer=ProductTypeSerializer(producttype,context={"request":request})
        return Response({"error":False,"message":"Single Data Fetch","data":serializer.data})


producttype_list=ProductTypeViewSet.as_view({"get":"list"})
producttype_create=ProductTypeViewSet.as_view({"post":"create"})
producttype_update=ProductTypeViewSet.as_view({"put":"update"})

class Product2ViewSet(viewsets.ModelViewSet):
    def list(self,request):  

        product2=Product2.objects.all()
        serializer=Product2Serializer(product2,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Product List Data","data":serializer.data}
        return Response(response_dict,)
        print(response_dict)

    def create(self,request):
        try:
           
            serializer=Product2Serializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"category Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"category During Saving Data"}
        return Response(dict_response)

    def update(self,request,pk=None):
        try:
            queryset=Product2.objects.all()
            product2=get_object_or_404(queryset,pk=pk)
            serializer=Product2Serializer(product2,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated Category Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating Category Data"}

        return Response(dict_response)

    def retrieve(self,request,pk=None):
        queryset=Product2.objects.all()
        product2=get_object_or_404(queryset,pk=pk)
        serializer=Product2Serializer(product2,context={"request":request})
        return Response({"error":False,"message":"Single Data Fetch","data":serializer.data})



product2_list= Product2ViewSet.as_view({"get":"list"})
product2_create= Product2ViewSet.as_view({"post":"create"})
product2_update= Product2ViewSet.as_view({"put":"update"})


"""def catlogsave(request):
    if request.method=='POST':
        productname=request.POST.get('productname')
        category=request.POST.get('category')  
        desc=request.POST.get('desc')
        price=request.POST.get('price')
        quantity =request.POST.get('quantity ')
        discountdesc=request.POST.get('discountdesc')
        oldprice=request.POST.get('oldprice')
        newdiscount=request.POST.get('newdiscount')
        img=request.POST.get('img')
        product={"productname":productname,'category':category,'desc':desc,'price':price,'quantity':quantity,'discountdesc':discountdesc,
        'oldprice':oldprice,'img':img}
        apipath=requests.post('http://127.0.0.1:8000/api/product/',json=product,content_type="application/json")
        return render(request,'dairy.html')
    else:

    
        return render(request,'dairy.html')"""

class RatingViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication] 
    permission_classes=[IsAuthenticated]
   # renderer_classes = [TemplateHTMLRenderer]
   # template_name = 'trial.html'
    def list(self,request):  
        rating=Rating.objects.all()
        serializer=RatingSerializer(rating,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Rating List Data","data":serializer.data}
        return Response(response_dict)
    

    def create(self,request):
        try:
           
            serializer=RatingSerializer(data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
          #  rating_id=serializer.data['id'];
          #  print(product_id,"ttttttttttt")
            dict_response={"error":False,"message":" Data Save Successfully"}
        except:
            dict_response={"error":True,"message":"Error During Saving Data"}
        return Response(dict_response)

    def update(self,request,pk=None):
        try:
            queryset=Rating.objects.all()
            rating=get_object_or_404(queryset,pk=pk)
            serializer=RatingSerializer(rating,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response={"error":False,"message":"Successfully Updated  Data"}
        except:
            dict_response={"error":True,"message":"Error During Updating C Data"}

        return Response(dict_response)

    def retrieve(self,request,pk=None):
        queryset=Rating.objects.all()
        rating=get_object_or_404(queryset,pk=pk)

        serializer=RatingSerializer(rating,context={"request":request})
        return Response({"error":False,"message":"Single Data Fetch","data":serializer.data})


rating_list=RatingViewSet.as_view({"get":"list"})
rating_create=RatingViewSet.as_view({"post":"create"})
rating_update=RatingViewSet.as_view({"put":"update"})