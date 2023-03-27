from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('exhibit/create/', views.create_exhibit, name='create_exhibit'),
    path('event/create/', views.create_event, name='create_event'),
    path('talent/create/', views.create_talent, name='create_talent'),
    path('review/create/', views.create_review, name='create_review'),
    path('favorite/<int:id>/<str:type>/',
         views.create_favorite, name='create_favorite'),
    path('review/delete/<int:id>/', views.delete_review, name='delete_review'),
]