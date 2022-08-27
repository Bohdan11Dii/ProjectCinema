from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cinema import settings
from user.views import user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('user/', include('user.urls')),
    path('', include('main_page.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


