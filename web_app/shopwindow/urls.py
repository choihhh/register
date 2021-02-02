from django.urls import path
from shopwindow.views import *

from myshop.views import HomeView, UserCreateView, UserCreateDoneTV

app_name = 'shopwindow'

urlpatterns = [
    #/product
    path('',ProductLV.as_view(),name= 'index'),
    #/<product:id>
    path('<int:pk>', ProductDV.as_view(), name='detail'), 

    path('accounts/', include('django.contrib.auth.urls')), 
    
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),



]
