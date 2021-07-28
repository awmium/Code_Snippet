#Media_settings

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#Media_setup_urls_pattern

from django.conf import settings
from django.conf.urls.static import static

#................
#................
#................

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)