
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^routes', include('routes.urls', namespace='routes')),
    url(r'^$', include('home.urls', namespace='home')),
]
