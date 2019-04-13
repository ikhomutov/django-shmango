from django.conf import settings
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(
        r'^terms/$',
        TemplateView.as_view(template_name='pages/terms.html'),
        name='terms'
    ),
    url(
        r'^privacy/$',
        TemplateView.as_view(template_name='pages/privacy.html'),
        name='privacy'
    ),
    url(
        r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name='about'
    ),
    url('', include(('users.urls', 'users'), namespace='users')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
