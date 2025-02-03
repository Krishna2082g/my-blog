from django.urls import path
from.views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView,post_detail

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post-detail'),
    path('post/new/', BlogCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post-delete'),
]
