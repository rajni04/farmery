from django.conf.urls.static import static
from farmeryy import settings
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib.auth.models import User
from django.urls import path
from farmeryyapp import views
from farmeryyapp.views import OTPAdmin
from django.urls import path,include
from .apiviews import user_list,product_list,user_create,category_list,producttype_list,product2_list,rating_list
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from farmeryyapp import apiviews,adminviews
from farmeryyapp.apiviews import InfoViewSet,LoginViewSet,ProductSerializer,Category1ViewSet,ProductTypeViewSet,Product2ViewSet,RatingViewSet

router=routers.DefaultRouter()
router.register('info',apiviews.InfoViewSet,basename="info")
#router.register('users',apiviews.UserViewSet,basename="user")
router.register('login',apiviews.LoginViewSet,basename="login")
router.register('product',apiviews.ProductViewSet,basename="product")
router.register('category',apiviews.Category1ViewSet,basename="category")
router.register('producttype',apiviews.ProductTypeViewSet,basename="producttype")
router.register('product2',apiviews.Product2ViewSet,basename="product2")
router.register('rating',apiviews.RatingViewSet,basename="rating")



admin_site=OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice)
urlpatterns=[
    path('home',views.index, name='home'),
    path('home1',views.home1, name='home1'),
    path('',views.home,name='homedesign'),
   # path('',include('rest_framework.urls')),
    path("homeadmin_template",views.homeadmin_template, name="homeadmin_template"),
    path('about',views.about, name="about"),
  
    path('admine/', admin_site.urls),
    path('how-it-works',views.work, name="how-it-works"),
    path('catalog/',views.catalog, name="catalog"),
    path('shop',views.shop, name="shop"),
    path('trial',views.trial, name="trial"),
    path('trialform',views.trialform, name="trialform"),
  
    path('info/cre',user_create ,name="info/cre"),
    #path('info/',views.user_list, name="info"),
    #path('register',views.register, name="register"),
    path('login',views.loginn, name="login"),
   # path('indexsign',views.indexsign, name="indexsign"),
    path('loogout', views.loogout,name="loogout"),
    path('mylogin',views.mylogin, name="mylogin"),
    path('register',views.register, name="register"),
   # path('loginform',views.loginform, name="loginform"),
    path('loginform',views.loginform, name="loginform"),


#product producr product 
    path('product',views.product, name="product"),
    path('viewproduct',views.viewproduct, name="viewproduct"),
    path('delete/<str:product_id>/', views.delete_product, name="delete"),
   # path('edit_product/<str:product_id>/', views.edit_product, name="edit_product"),





#-----------------------------------------------------------------------------------------------------------------------------------------
    # api url



    path('api/',include(router.urls)),
   # path('api/auth/',obtain_auth_token),
    path('api/auth/',obtain_auth_token),
    path('api/product/',product_list , name="product"),
   # path('api/catalog/',apiviews.catlogsave, name="api/catalog"),
    path('api/category/',category_list, name="category"),
    path('api/producttype/',producttype_list, name="api/producttype"),
    path('api/product2/',product2_list, name="api/product2"),
    path('api/rating/',rating_list, name="api/rating"),




    path('info/',user_list , name="info"),



    #-------------------------------adminviews.py.....................................................



    path('product',adminviews.product, name="product"),
    path('product_save',adminviews.product_save, name="product_save"),
    path('product_details/<str:myid>/',adminviews.product_details, name="product_details"),
    path('edit_product/<str:product_id>/',  adminviews.edit_product,name="edit_product"),
    path('product_edit_save', adminviews.product_edit_save),
    path('delete_product/<str:product_id>/', adminviews.delete_product),
    path('team',adminviews.team, name="team"),
    path('blog',views.blog, name="blog"),
    path('team_save', adminviews.team_save),
    path('viewteam',adminviews.viewteam,name="viewteam"),
    path('teamHome',views.teamHome, name="team"),

    path('category',adminviews.category, name="category"),
    path('category_save', adminviews.category_save),
    path('viewcategory',adminviews.viewcategory, name="viewcategory"),
    path('viewFruitGrocery',views.viewFruitGrocery, name="viewFruitGrocery"),
    path('edit_category/<str:category_id>/',  adminviews.edit_category,name="edit_category"),
    path('edit_category_save', adminviews.edit_category_save),
    path('delete_category/<str:category_id>/', adminviews.delete_category),
    path('subcategory',adminviews.subcategory, name="subcategory"),
    path('subcategory_save',adminviews.subcategory_save, name="subcategory_save"),
    path('viewsubcategory',adminviews.viewsubcategory, name="viewsubcategory"),
    path('fruitGrocery',adminviews.fruitGrocery, name="fruitGrocery"),
    path('fruitGrocery_save', adminviews.fruitGrocery_save),
    path('fetch_api/<category_id>', adminviews.fetch_api, name="fetch_api"),
    path('edit_subcategory/<str:subcategory_id>/',adminviews.edit_subcategory, name="edit_subcategory"),
    path('delete_subcategory/<str:subcategory_id>/',adminviews.delete_subcategory, name="delete_subcategory"),
    path('loogout', views.loogout,name="loogout"),
    path('howit_work',adminviews.howit_work, name="howit_work"),
    path('howit_work_save',adminviews.howit_work_save, name="howit_work_save"),
    path('viewworkdata',adminviews.viewworkdata, name="viewworkdata"),
    path('delete_viewworkdata/<str:work_id>/', adminviews.delete_viewworkdata,name="delete_viewworkdata"),
    path('sliderhome',adminviews.sliderhome, name="sliderhome"),
    path('sliderhome_save',adminviews.sliderhome_save, name="sliderhome_save"),
    path('delete_slider/<str:sliderhome_id>/', adminviews.delete_slider,name="delete_slider"),
    path('viewslider',adminviews.viewslider, name="viewslider"),

    path('content',adminviews.content, name="content"),
    path('content_save',adminviews.content_save, name="content_save"),

    path('contentview',adminviews.contentview, name="contentview"),
    path('delete_content/<str:content_id>/', adminviews.delete_content),

    path('homeabout',adminviews.homeabout, name="homeabout"),
    path('offerhomeproduct', adminviews.offerhomeproduct),
    path('offerhomeproduct_save', adminviews.offerhomeproduct_save),

 



    ]