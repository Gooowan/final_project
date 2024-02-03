from django.urls import path
from playlists import views

urlpatterns = [
    path('', views.entity_list, name='playlists_list'),
    path('<int:id>/', views.entity_detail, name='playlists_detail'),
    path('create/', views.entity_create, name='playlists_create'),
    path('delete/<int:id>/', views.entity_delete, name='playlists_delete'),
]
