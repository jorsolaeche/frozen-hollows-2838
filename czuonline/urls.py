from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Inicio
	url(r'^', include('guiaczu.urls', namespace='guiaczu')),
    #Archivos/imagenes
    url(r'^documents/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    #Admin
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += patterns('',
 (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
 )

