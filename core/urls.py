"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from filter.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('gallery/', gallery, name='gallery'),
    path('detail/<int:id>/', photo_detail, name='detail'),
    path('filter1/<int:id>/', filter1, name='filter1'),
    path('filter2/<int:id>/', filter2, name='filter2'),
    path('filter3/<int:id>/', filter3, name='filter3'),
    path('filter4/<int:id>/', filter4, name='filter4'),
    path('editted_gallery/', editted_gallery, name='editted_gallery'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)