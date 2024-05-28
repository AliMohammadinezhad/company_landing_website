from django.urls import path

from . import views

app_name = 'landing'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('inner/', views.inner_view, name='inner')
    
]
