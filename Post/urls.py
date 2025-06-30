from django.conf.urls.static import static
from django.urls import path, include

from django.conf import settings
from Post.settings import DEBUG

urlpatterns = [
    path('', include('app.urls')),
    path('auth/', include('authenticate.urls')),
    path('i18n/', include('django.conf.urls.i18n')),

]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT      )
