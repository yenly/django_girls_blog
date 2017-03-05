from django.conf.urls import url
from . import views

urlpatterns = [
    # this pattern will tell Django that view.post_list to go http://127.0.0.1:8000
    url(r'^$', views.post_list, name='post_list'),
]
