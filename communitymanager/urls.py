from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('communities', views.communities, name='communities'),
    path('community/<int:id>', views.community, name='community')
    ]
