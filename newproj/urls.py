"""
URL configuration for newproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from newproj import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('rent/', views.rent, name="rent"),
    path('about/', views.about, name="about"),
    path('ride/', views.ride, name="ride"),
    path('userform/', views.userForm),
    path('submitform/', views.submitForm, name="submitform"),
    path('service/', views.service, name="services"),
    path('signup/', views.signup, name="signup"),
 
    path('course/<slug:courseid>', views.courseDetails),
 

]
