from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path(
        '',
        include(
            ('shmango.apps.accounts.urls', 'accounts'), namespace='accounts'
        ),
    ),
    path(
        '',
        include(
            ('shmango.apps.registration.urls', 'registration'),
            namespace='registration'
        ),
    ),
    path('oauth/', include('social_django.urls', namespace='social')),
    path(
        'terms/',
        TemplateView.as_view(template_name='pages/terms.html'),
        name='terms'
    ),
    path(
        'privacy/',
        TemplateView.as_view(template_name='pages/privacy.html'),
        name='privacy'
    ),
    path(
        'about/',
        TemplateView.as_view(template_name='pages/about.html'),
        name='about'
    ),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
