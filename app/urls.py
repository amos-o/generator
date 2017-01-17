from django.conf.urls import url
from .views import GeneratorView, IndexView


urlpatterns = [
    url(r'^generate/$', GeneratorView.as_view(), name='generate'),
    url(r'^$', IndexView.as_view(), name='index')
]
