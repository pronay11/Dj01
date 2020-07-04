from django.contrib import admin
from django.urls import path
from .views import student_list,student_detail



urlpatterns = [
   path('list/',student_list,name='student_list'), 
   path('detail/<int:id>',student_detail,name='student_detail'),
    
]
 
