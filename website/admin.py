from django.contrib import admin
from .models import Student
# from .models import Website

# Register your models here.
# class WebsiteAdmin(admin.ModelAdmin):
#     list_display=('name','working','phone')
#     list_editable=('working')
#     search_fields=('name')
#     list_filter=['working']
    
# admin.site.register(Student,WebsiteAdmin)
admin.site.register(Student)
