from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'miproyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'', include('miapp.urls')),
    # url(r'^$', views.index),	

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('miapp.urls')),

]
	

