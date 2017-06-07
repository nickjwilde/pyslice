from django.conf.urls import url

from . import views

app_name = 'pyslice'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^learn/$', views.learn, name='learn'),
]
