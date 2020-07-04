from django.contrib import admin
from .models import StudentInfo
class StudentInfoAdmin(admin.ModelAdmin):
    List_display=['roll','name']

admin.site.register(StudentInfo,StudentInfoAdmin)
