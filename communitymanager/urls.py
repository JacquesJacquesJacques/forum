from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('communities', views.communities, name='communities'),
    path('community/<int:id>', views.community, name='community'),
    path('post/<int:id>', views.post, name='post'),
    path('post/creation', views.post_creation, name="post_creation"),
    path('post/edition/<int:id>', views.post_edit, name="post_edit"),
    path('communities/<int:id>', views.subscribe, name="subscribe"),
    path('community/<int:id>', views.show_comments, name="show_comments")
    ]
