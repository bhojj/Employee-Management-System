"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from.views import *
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = "Employee Management System"
admin.site.site_title = "Emp Admin Portal"
admin.site.index_title = "Welcome to Employee Management System"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('index/' ,home),
    path('about/' ,about),
    path('services/' ,services),
    path('emp/',include('emp.urls')),
    # path('authentication/',include("authentication.urls")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
