from django.urls import include, path  # Import path instead of url
from django.contrib import admin

urlpatterns = [
    path('riddles/', include('riddles.urls')),  # No need for name argument here
    path('admin/', admin.site.urls),
]
