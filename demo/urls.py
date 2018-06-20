from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^login$', views.home, name='home'),
    url(r'^process$', views.process, name='process'),
    url(r'^detail$', views.detail, name='detail'),
    url(r'^data$', views.data, name='data'),
    url(r'^add$', views.add, name='add'),
    url(r'^info$', views.info, name='info'),
    url(r'^registration$', views.registration, name='registration'),



]