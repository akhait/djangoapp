from django.conf.urls import url
from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^(?P<task_id>\d+)/done', views.done, name='done'),
    url(r'^(?P<pk>\d+)', views.DetailView.as_view(), name='detail'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
