from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$',views.home,name='home'),
    url(r'^projects/(\d+)',views.projects,name='projects'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url('^uploads/',views.post_site,name='post_site'),