from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('', wall_main),
    url('like/', like, name='like'),
    path('<str:wall_name>/', wall_detail,name='wall_detail'),
    

]
