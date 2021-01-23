from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),
]  # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# To facilitate the uploads of media files to the website... To help create the media url for an image file.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
