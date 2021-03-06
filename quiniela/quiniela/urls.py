from django.conf.urls import patterns, include, url
from quiniela.views import home, guardarUsuario, iniciarSesion, procesar, verp
from django.contrib import admin
admin.autodiscover()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quiniela.views.home', name='home'),
    # url(r'^quiniela/', include('quiniela.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^creacioncuenta/',guardarUsuario),
    url(r'^iniciarsesion/',iniciarSesion),
    url(r'^procesarquiniela/',procesar),
    url(r'^verpredicc/',verp),
    url(r'^home/',home),
)
