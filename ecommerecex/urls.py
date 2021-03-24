from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Apps url
    path('', include('apps.core.urls')),
    path('vendors/', include('apps.vendor.urls')),
]
