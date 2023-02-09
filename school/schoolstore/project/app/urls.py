from django.contrib import admin
from django.urls import path,include
from .import views
from .views import load_courses

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('index/',views.index,name='index'),
    path('load-courses/',load_courses,name='ajax_load_courses'),
    path('message/', views.message, name='message'),
    path('logout',views.logout,name='logout')

]