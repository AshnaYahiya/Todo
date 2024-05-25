"""
URL configuration for Todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from work.views import Registration,Sighnin
from work.views import Add_task, Delete_task
from work.views import Task_edit,Logout,user_delete
from work.views import update_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    
    path('user/',Registration.as_view()),
    path('log/',Sighnin.as_view(),name='signin'),
    path('',Add_task.as_view(),name="reg"),
    path('delete/<int:pk>', Delete_task.as_view(),name="delete"),
    path('task/update/<int:pk>',Task_edit.as_view(),name='edit'),
    path('logout/',Logout.as_view(),name='logout'),
    path('usdel/<int:pk>',user_delete.as_view(),name='del'),
    path('editprofile/<int:pk>',update_user.as_view()),

]
