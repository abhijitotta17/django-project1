from django.contrib import admin

# Register your models here.
from demo1.models import ModelStudent
class StudAdminModel(admin.ModelAdmin):
    list_display=['regid','name','marks','email','phone']
admin.site.register(ModelStudent,StudAdminModel)