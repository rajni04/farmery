from django.contrib import messages 
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from farmeryyapp.models import Product
from django.urls import reverse
from .models import *
from farmeryyapp.models import Subcategory
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, logout
from django.core.paginator import Paginator



def homeadmin_template(request):
    product_count=Product.objects.all().count()
    category_count=Category1.objects.all().count()
    
    print(product_count,'hnhhhhhhhhhhdbbbbbwddd')

    return render(request,'Admin/homeadmin_template.html',{"category_count":category_count,"product_count":product_count})




def product(request):  
    product=Product.objects.all()
    return render(request,"Admin/Product.html",{"product":product})
    
def product_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
    
        productname =request.POST.get("productname")
        categoryy=request.POST.get("categoryy")
        desc=request.POST.get("desc")
        price =request.POST.get("price") 
        quantity =request.POST.get("quantity")
        discountdesc=request.POST.get("discountdesc")
        oldprice =request.POST.get("oldprice")
           
        newdiscount=request.POST.get("newdiscount")
        img=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        img=fs.url(filename)
           
        #try:
        product=Product(productname=productname,categoryy=categoryy,desc=desc,price=price,quantity=quantity,discountdesc=discountdesc,oldprice=oldprice,newdiscount=newdiscount,img=img)
            

        product.save()
        messages.success(request,"Successfully Added ")
        return HttpResponseRedirect("product")
        #except:
            #messages.error(request,"Failed to Add ")
            #return HttpResponseRedirect("product")

def product_details(request,myid):
    #Fetch the product using Id
    product=Product.objects.filter(id=myid)
    print(product,'hnhhhhhhhhhhdbbbbbwddd')
    return render(request,'Productdetail.html',{'product':product[0]}) 



def edit_product(request,product_id):
    product=Product.objects.get(id=product_id)
    return render(request,"Admin/EditProduct.html",{"product":product})

def product_edit_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        product_id=request.POST.get("product_id")
        productname =request.POST.get("productname")
        category=request.POST.get("category")
        desc=request.POST.get("desc")
        price =request.POST.get("price") 
        quantity =request.POST.get("quantity")
        discountdesc=request.POST.get("discountdesc")
        oldprice =request.POST.get("oldprice")
           
        newdiscount=request.POST.get("newdiscount")
        try:
            product=Product.objects.get(id=product_id)
            product.productname=productname
            product.category=category
            product.desc=desc
            product.price=price
            product.quantity=quantity
            product.discountdesc=discountdesc
            product.oldprice=oldprice
            product.save()
        
            messages.success(request,"Successfully Edited ")
            return HttpResponseRedirect(reverse("farmeryyapp/edit_product",kwargs={"product_id":product_id}))
        except:
            messages.error(request,"Failed to Edit ")
            return HttpResponseRedirect(reverse("edit_product",kwargs={"product_id":product_id}))

def delete_product(request,product_id):    
  product=Product.objects.all()
  product.delete()
  return redirect("/viewproduct")

def team(request):
    team =Team.objects.all()
    context={'team':team}
    return render(request,'Admin/team.html',context)

def team_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
    
        tname =request.POST.get("tname")
        tdesc=request.POST.get("tdesc")
        tabt=request.POST.get("tabt")
       
        timg=request.FILES['timg']
        fs=FileSystemStorage()
        filename=fs.save(timg.name,timg)
        timg=fs.url(filename)
           
       # try:
        team=Team(tname=tname,tabt=tabt,tdesc=tdesc,timg=timg)
            

        team.save()
        messages.success(request,"Successfully Added ")
        return HttpResponseRedirect("team")
        #except:
            #messages.error(request,"Failed to Add ")
            #return HttpResponseRedirect("team")

def viewteam(request):
    team=Team.objects.all()
    return render(request,"Admin/ViewTeam.html",{'team':team})


def category(request):  
    category=Category1.objects.all()
    
    return render(request,"Admin/Category.html",{"category":category})

def category_save(request):  
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
    
        cattype =request.POST.get("cattype")
           
        #try:
        category=Category1(cattype=cattype)
            

        category.save()
        messages.success(request,"Successfully Added ")
        return HttpResponseRedirect("category")
        #except:
            #messages.error(request,"Failed to Add ")
            #return HttpResponseRedirect("category")

def viewcategory(request):
    category=Category1.objects.all().order_by('cattype').distinct('cattype')
    
    all_cat = Paginator(category,5)# Show 25 contacts per page.
    

    page = request.GET.get('page')
    try:
        # create Page object for the given page
        page_obj = all_cat.page(page)
    except PageNotAnInteger:
        # if page parameter in the query string is not available, return the first page
        page_obj = all_cat.page(1)
    except EmptyPage:
        # if the value of the page parameter exceeds num_pages then return the last page
        page_obj= all_cat.page(all_cat.num_pages)
   
    return render(request,"Admin/CategoryView.html", {'category':category,'page_obj': page_obj})
    print(page_obj)

def edit_category(request,category_id):
    category=Category1.objects.get(id=category_id)
    return render(request,"Admin/EditCategory.html",{"category":category})

def edit_category_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        category_id=request.POST.get("category_id")
        cattype =request.POST.get("cattype")
        
        try:
            category=Category1.objects.get(id=category_id)
            category.cattype=cattype
            category.save()
        
            messages.success(request,"Successfully Edited ")
            return HttpResponseRedirect(reverse("farmeryyapp/edit_category",kwargs={"category_id":category_id}))
        except:
            messages.error(request,"Failed to Edit ")
            return HttpResponseRedirect(reverse("edit_category",kwargs={"category_id":category_id}))

def delete_category(request,category_id):    
  category=Category1.objects.get(id=category_id)
  category.delete()
  return redirect("/viewcategory")


def subcategory(request): 
    category=Category1.objects.all() 
   
    return render(request,"Admin/SubCategory.html",{"category":category})


def subcategory_save(request): 
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subcategory_name=request.POST.get("subcategory_name")
        category_id=request.POST.get("category")
        category=Category1.objects.get(id=category_id)
        
        try:
            subcategory=Subcategory(subcategory_name=subcategory_name,category_id=category)
            subcategory.save()
            messages.success(request,"Successfully Added ")
            return HttpResponseRedirect(reverse("subcategory"))
        except:
            messages.error(request,"Failed to Add ")
            return HttpResponseRedirect(reverse("subcategory"))

def viewsubcategory(request):
    subcategory=Subcategory.objects.all()
    paginate_by = 2

    return render(request,"Admin/ViewSubCategory.html",{'subcategory':subcategory})
   



def fruitGrocery(request):  
   
    category=Category1.objects.all() 
    subcategory=Subcategory.objects.all()
    
    return render(request,"Admin/FruitAndGrocery.html",{'category':category,'subcategory':subcategory})
    
def fruitGrocery_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        category_id=request.POST.get("category")
        category_obj=Category1.objects.get(id=category_id)
        subcategory_id=request.POST.get("subcategory")
        subcategory_obj=Subcategory.objects.get(id=subcategory_id)
        proname =request.POST.get("proname")
        pric=request.POST.get("pric")
        quant=request.POST.get("quant")
       
        farmer_name =request.POST.get("farmer_name")
        orchard=request.POST.get("orchard")
        expted_delivery =request.POST.get("expted_delivery")
           
        pre_delivery=request.POST.get("pre_delivery")
        img=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        img=fs.url(filename)
           
       # try:
        product2=Product2(proname=proname,category_id=category_obj,subcategory_id=subcategory_obj,pric=pric,quant=quant,farmer_name=farmer_name,orchard=orchard,expted_delivery=expted_delivery,pre_delivery=pre_delivery,img=img)
       
        product2.save()
        messages.success(request,"Successfully Added ")
        return HttpResponseRedirect("fruitGrocery")
       # except:
        #messages.error(request,"Failed to Add ")
        #return HttpResponseRedirect("fruitGrocery")

from django.http import JsonResponse, HttpResponse
from django.core import serializers
import json
def fetch_api(request, category_id):
    cat=Category1.objects.get(id=category_id).subcategory_set.all()
    print(Category1.objects.get(id=category_id).subcategory_set.all())
    data=[]
    for i in cat:
        data.append({"id":i.pk, "subcategory_name":i.subcategory_name})
    
    # data=serializers.serialize(
    #                 'json', data)
    print(data)
    return HttpResponse(json.dumps(data), content_type="application/json")

def edit_subcategory(request,subcategory_id): 
   category=Category1.objects.all()
   subcategory=Subcategory.objects.get(id=subcategory_id)
   return render(request,"Admin/Edit_Subcategory.html",{"subcategory":subcategory,"category":category})

def edit_subcategory_save(request): 
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        subcategory_id=request.POST.get("subcategory_id")
        subcategory_name=request.POST.get("subcategory_name")
        category_id=request.POST.get("category")
        

        try:
            subcategory=Subcategory.objects.get(id=subcategory_id)
            subcategory.subcategory_name=subcategory_name
            
            
            category=Category1.objects.get(id=category_id)
            subcategory.category_id=category
            subcategory.save()

            messages.success(request,"Successfully Edited ")
            return HttpResponseRedirect(reverse("edit_subcategory",kwargs={"subcategory_id":subcategory_id}))
        except:
            messages.error(request,"Failed to Edit ")
            return HttpResponseRedirect(reverse("edit_subcategory",kwargs={"subcategory_id":subcategory_id}))

def delete_subcategory(request,subcategory_id):    
  subcategory=Subcategory.objects.get(id=subcategory_id)
  subcategory.delete()
  return redirect("/viewsubcategory")
