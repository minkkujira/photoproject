
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include #include 追加

urlpatterns = [
    path('admin/', admin.site.urls),

    # photo.urlsへのurlパターン
    path('', include('photo.urls')),

    # accounts.urlsへのURLパターン
    path('', include('accounts.urls')),
]
