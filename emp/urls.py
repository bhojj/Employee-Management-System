from django.contrib import admin
from django.urls import path,include
from.views import *


urlpatterns = [
    path('home/',emp_home),
    path('add-emp/',add_emp),
    path('delete-emp/<int:emp_id>',delete_emp),
    path('update-emp/<int:emp_id>',update_emp),
    path('do-update-emp/<int:emp_id>' ,do_update_emp),
    path('testimonials/',testimonials),
    path('feedback/',feedback),
    
    # path("users/login/",name="users.login"),
    # path('login/',emp_login),

#     path('admin/', admin.site.urls),
#     path('',home),
#     path('index/' ,home),
#     path('about/' ,about),
#     path('services/' ,services),
#     path('student/',include('emp.urls'))

]