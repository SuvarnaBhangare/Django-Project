from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
   path('', views.index1, name='index1'),
   path('<int:album_id>/', views.detail, name='detail'),
   path('<int:album_id>/results/', views.results, name='results')
   

   # path(r'^(?P<album_id>[0-9]+)/$', views.details, name='details'),
]