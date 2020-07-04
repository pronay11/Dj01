from django.contrib import admin
from .models import Post
class PostAdmin(admin.ModelAdmin):
    List_display=['tittle','description','created_dt']

admin.site.register(Post,PostAdmin)

