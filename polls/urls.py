from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^(?P<pk>\d+)/results', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote', views.vote, name='vote'),
    url(r'^(?P<pk>\d+)', views.DetailView.as_view(), name='detail'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
