from django.contrib import admin
from django.urls import path, include
from imsApp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('imsApp.urls')),
    path('accounts/login/', views.login_view, name ='login'),
    path('accounts/logout/', views.logout_view, name ='logout'),
]
