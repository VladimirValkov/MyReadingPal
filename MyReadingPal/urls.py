from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyReadingPal.home.urls')),
    path('book/', include('MyReadingPal.books.urls')),
]
