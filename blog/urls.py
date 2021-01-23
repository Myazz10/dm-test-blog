from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    DeletePostView,
    UpdatePostView,
    AddPostView,
    AddCategoryView,
    post_by_category_list_view,
    like_view,
    AddCommentView,
)


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post-details/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('update-post/<int:pk>/', UpdatePostView.as_view(), name='update-post'),
    path('delete-post/<int:pk>/remove', DeletePostView.as_view(), name='delete-post'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    path('category/<int:pk>/', post_by_category_list_view, name='category'),
    path('like/<int:pk>/', like_view, name='like_post'),
    path('<int:pk>/add-comment/', AddCommentView.as_view(), name='add-comment'),
]
