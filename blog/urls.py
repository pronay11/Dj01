from django.contrib import admin
from django.urls import path
from .views import post_list,post_detail,home



urlpatterns = [
   path('post_list/',post_list,name='post_list'), 
   path('post_detail/<int:id>',post_detail,name='post_detail'),
   path('',home,name='home'),
    
]
 