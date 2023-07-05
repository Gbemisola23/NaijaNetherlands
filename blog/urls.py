from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path('contactus/', include('contactus.urls')),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/edit-comment/<slug:commentId>/', views.PostDetail.as_view(), name='edit_comment'),
    path('<slug:slug>/delete-comment/<slug:commentId>', views.DeleteComment.as_view(), name="delete_comment"),
    path('<slug:slug>/like', views.PostLike.as_view(), name='post_like'),
]
