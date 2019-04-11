from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
