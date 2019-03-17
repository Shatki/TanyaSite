"""Tatyana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from experience.views import awards
import website.views as pages
from gallery.views import gallery_list, gallery_detail
from news.views import news_list, news_detail, comment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', pages.about),
    path('about/awards/', awards),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('gallery/', gallery_list),
    path('gallery/<directory>/', gallery_detail),
    path('news/', news_list),
    path('news/<news_id>/', news_detail),
    path('news/<news_id>/comment/', comment),


    path('<menu>/<url>/', pages.page_dispatcher),
    path('', pages.about),
    # path('users/<username>/photo/', users.get_photo),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + staticfiles_urlpatterns()
