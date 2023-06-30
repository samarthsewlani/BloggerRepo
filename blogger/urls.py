"""blogger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from blogs.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('',include('users.urls')),
    path('home/', home, name='home'),
    path('category/', category, name='category'),
    path('contact/', contact, name='contact'),
    path('create_blog/',create_blog, name='create_blog'),
    path('blogs/', bloglist, name='bloglist'),
    path('blog/<int:bid>/', blog_detail, name='blogdetail'),
    path('blog/detail/<int:bid>/', blog_detail_new, name='blog_detail_new'),
    path('blog/update/<int:bid>/', update_blog,name='update_blog'),
    path('blog/delete/confirm/<int:bid>/', confirm_delete, name='confirm_delete'),
    path('blog/delete/<int:bid>/', delete, name='delete'),
    
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)