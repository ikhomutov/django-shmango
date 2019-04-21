from django.urls import path

from .views import index_view
from .views import login_view
from .views import logout_view
from .views import password_change_done_view
from .views import password_change_view
from .views import signup_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('password_change/', password_change_view, name='password_change'),
    path(
        'password_change_done/',
        password_change_done_view,
        name='password_change_done'
    ),
    path('', index_view, name='index')
]
