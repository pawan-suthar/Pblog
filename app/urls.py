from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from.views import *

urlpatterns = [
    path("",home),
    path('blog/<slug:url>', post),
    path('category/<slug:url>',category)
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

