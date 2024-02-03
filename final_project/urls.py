from django.contrib import admin
from django.urls import path, include
from final_project import views

urlpatterns = [
    path('', views.main_page, name='main-page'),
    path('playlist/', include('playlists.urls')),
]
