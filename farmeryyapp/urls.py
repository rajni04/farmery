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
from farmeryyapp import apiviews
from farmeryyapp.apiviews import InfoViewSet, UserViewSet,LoginViewSet,ProductSerializer,Category1ViewSet,ProductTypeViewSet,Product2ViewSet,RatingViewSet

router=routers.DefaultRouter()
router.register('info',apiviews.InfoViewSet,basename="info")
router.register('users',apiviews.UserViewSet,basename="user")
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
    path('',views.home,name='homedesign'),
   # path('',include('rest_framework.urls')),
    path("homeadmin_template",views.homeadmin_template, name="homeadmin_template"),
    path('about',views.about, name="about"),
     path('product',views.product, name="product"),
    path('admine/', admin_site.urls),
    path('how-it-works',views.work, name="how-it-works"),
    path('catalog/',views.catalog, name="catalog"),
    path('shop',views.shop, name="shop"),
    path('trial',views.trial, name="trial"),
    path('trialform',views.trialform, name="trialform"),
    path('team',views.team, name="team"),
    path('info/cre',user_create ,name="info/cre"),
    #path('info/',views.user_list, name="info"),
    #path('register',views.register, name="register"),
    path('login',views.loginn, name="login"),
    path('mylogin',views.myloginn, name="mylogin"),
   # path('loginform',views.loginform, name="loginform"),
    path('loginform',views.loginform, name="loginform"),


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
   
    ]