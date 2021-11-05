from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('post/listview/', PostListView.as_view(), name='post_listview'),
    path('post/detailview/<int:pk>/', PostDetailView.as_view(), name='post_detailview'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
   

]
