from django.contrib import admin
from django.urls import path
from .views import district_list,district_detail



urlpatterns = [
   path('district_list/',district_list,name='district_list'), 
   path('district_detail/<int:id>',district_detail,name='district_detail'),
    
]