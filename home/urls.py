from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/', views.loginUser, name='login'),
    url(r'^signout/', views.logoutUser, name='logout'),
]
