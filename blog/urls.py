from . import views
from django.urls import path


urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path("about/", views.about, name="about"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('delete-comment/<slug:slug>/<int:id>', views.DeleteComment.as_view(), name="delete_comment"),
    path('edit-comment/<slug:slug>/<int:id>', views.EditComment.as_view(), name='edit_comment'),
]
