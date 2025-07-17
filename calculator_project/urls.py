
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls), #Important in django
    path('',include('calci.urls'))
]
