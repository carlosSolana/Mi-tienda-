from django.conf.urls import url
from miapp import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
	url(r'^(?P<videojuego_id>\d+)/$',views.detalle_videojuego, name='detalle_videojuego'),
	 url(r'^registro$', views.registro, name='registro'),
    url(r'^login$', views.loginpage, name='login'),
    url(r'^logout$', views.logoutpage, name='logout'),
		
]

