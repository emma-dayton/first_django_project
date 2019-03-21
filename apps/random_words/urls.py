from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^random_word$', views.index),
  url(r'^random_word/new$', views.generate_random_word),
  url(r'^random_word/clear$', views.clear),

]
