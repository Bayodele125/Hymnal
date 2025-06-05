from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('hymn/<int:hymn_id>/', views.hymn_detail, name='hymn_detail'),
    path('about/', views.about, name='about'),
]
