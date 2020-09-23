from django.urls import path
from . import views

urlpatterns = [
    path('url_list/', views.url_list, name='url_list'),
    path('', views.base_view, name='base'),

]