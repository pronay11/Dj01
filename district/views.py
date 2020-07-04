from django.shortcuts import render
from .models import DistrictInfo

def district_list(request):
   
    information = DistrictInfo.objects.all()
    context={
        'district_list':information
    }
    return render(request,'district/district_list.html',context)

def district_detail(request,id):
   
    detail = DistrictInfo.objects.get(id=id)
    context={
        'detail':detail
    }
    return render(request,'district/district_detail.html',context)  
