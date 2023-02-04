from django.contrib import admin
from django.urls import path,include
from.views import *

urlpatterns = [
    path('home/',emp_home),
    path('add-emp/',add_emp),

#     path('admin/', admin.site.urls),
#     path('',home),
#     path('index/' ,home),
#     path('about/' ,about),
#     path('services/' ,services),
#     path('student/',include('emp.urls'))

]