from django.contrib import admin
from django.urls import path
from media_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),  # Points root to your gallery view
]