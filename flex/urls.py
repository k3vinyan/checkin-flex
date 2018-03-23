
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^routes/', include('routes.urls', namespace='routes')),
    url(r'^drivers/', include('drivers.urls', namespace='drivers')),
    url(r'^checkin/', include('checkin.urls', namespace='checkin')),
    url(r'^assignRoutes/', include('assignRoutes.urls', namespace='assignRoutes')),
    url(r'^checkout/', include('checkout.urls', namespace='checkout')),
    url(r'^$', include('home.urls', namespace='home')),
    url(r'^login/', include('home.urls', namespace='login')),
    url(r'^logout/', include('home.urls', namespace='logout')),
]
