from django.urls import path
from .views import *

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit/',ArticleUpdateView.as_view(), name='article_edit'), # new
    path('<int:pk>/',ArticleDetailView.as_view(), name='article_detail'), # new
    path('<int:pk>/delete/',ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('comment/<int:pk>/add/',CommentCreateView.as_view(), name='comment_new'),
]