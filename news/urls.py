from django.urls import path
from .views import home, ArticleListCreateView, ArticleDetailView

urlpatterns = [
    path('', home, name='home'),
    path('articles/', ArticleListCreateView.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
