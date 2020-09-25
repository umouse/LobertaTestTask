from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_view, name='base'),
    path('urls/<int:id>/', views.url_status_code, name='url_status_code'),

]