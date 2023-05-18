from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('urls.urls')),
    path('api/', include('api.urls')),
]


handler404 = 'urls.views.page_not_found_view'
