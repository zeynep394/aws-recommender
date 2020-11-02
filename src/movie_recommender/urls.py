from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from post.views import website,post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',website),
    path('post/<id>/', post, name='post-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)