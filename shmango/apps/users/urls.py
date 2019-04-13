from django.conf.urls import url

from .views import login_view
from .views import logout_view
from .views import signup_view

urlpatterns = [
    url('login/', login_view, name='login'),
    url('logout/', logout_view, name='logout'),
    url('signup/', signup_view, name='signup'),
]
