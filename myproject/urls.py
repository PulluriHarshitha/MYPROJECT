"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from my_app import views

# ' ' == http://127.0.0.1:8000
# ' ' means http://127.0.01:8000/login

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('login/', views.user_login, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('logout-post/',views.user_logout, name='logout'),
    path('display-post/',views.display_post, name='display-post'),
    path('read-post/<int:id>/',views.read_post, name='read-post'),
    path('add-post/',views.add_post, name ='add-post')
    
    ]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
