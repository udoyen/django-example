from django.urls import path, re_path  # Import path and re_path instead of url

from . import views

app_name = 'riddles'

urlpatterns = [
    path('', views.index, name='index'),  # No regex needed for the root path
    re_path(r'^(?P<riddle_id>[0-9]+)/$', views.detail, name='detail'),  # Use re_path for regex
    re_path(r'^(?P<riddle_id>[0-9]+)/answer/$', views.answer, name='answer')
]
