from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^addcourse$', views.addcourse),
    url(r'^destroy/(?P<course_id>\d+)$', views.destroy),
    url(r'^confirmdestroy/(?P<course_id>\d+)$', views.confirmdestroy),
]
