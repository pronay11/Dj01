from django.shortcuts import render
from .models import StudentInfo

def student_list(request):
   
    info = StudentInfo.objects.all()
    context={
        'student_list':info
    }
    return render(request,'student/student_list.html',context)

def student_detail(request,id):
   
    detail_info = StudentInfo.objects.get(id=id)
    context={
        'detail_info':detail_info
    }
    return render(request,'student/student_detail.html',context)    




