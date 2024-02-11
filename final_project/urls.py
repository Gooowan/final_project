from django.contrib import admin
from django.urls import path, include
from final_project import views
from final_project.consumer import YourConsumer

urlpatterns = [
    path('', views.main_page, name='main-page'),
    path('playlist/', include('playlists.urls')),
    path('cookie/set/', views.set_cookie, name='set-cookie'),
    path('cookie/get/<str:cookie_name>/', views.get_cookie, name='get-cookie'),
    path('header/set/', views.set_header, name='set_header'),
    path('header/get/<str:header_name>/', views.get_header, name='get_header'),

    path('ws', views.sendHTML, name='sendHTML'),
]
