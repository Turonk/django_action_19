from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('myapp.urls'), namespace='myapp'),
    path('admin/', admin.site.urls),
]
