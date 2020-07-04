from django.contrib import admin
from .models import DistrictInfo
class DistrictInfoAdmin(admin.ModelAdmin):
    List_display=['name']

admin.site.register(DistrictInfo,DistrictInfoAdmin)


