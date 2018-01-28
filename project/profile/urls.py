from django.contrib import admin
from django.urls import path

from . import views

app_name = 'profile'

urlpatterns = [
    path('index/',
         views.index,
         name = 'index'),
    path('login/',
         # 'django.contrib.auth.views.login',
         views.login,
         # kwargs={'template_name': 'profile/login.html'},
         name='login'),
    path('verify/',
         views.verify,
         name = 'verify'),
    path('logout/',
         # 'django.contrib.auth.views.logout',
         views.logout,
         # kwargs={'template_name': 'profile/logout.html'},
         name='logout'),
    path('register/',
         # 'django.contrib.auth.views.logout',
         views.register,
         # kwargs={'template_name': 'profile/logout.html'},
         name='register'),
    # path('update/', views.update, name='update')
]