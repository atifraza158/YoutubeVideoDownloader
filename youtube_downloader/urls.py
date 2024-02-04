from django.contrib import admin
from django.urls import path
from youtube.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', youtube_downloader, name='home'),
]
