from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls', namespace='index')),
    path('admin/', admin.site.urls),
]
