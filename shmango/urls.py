from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
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
    path('', include(('shmango.apps.users.urls', 'users'), namespace='users')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
