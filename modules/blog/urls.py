from django.urls import path
from .views import ArcticleListView, ArticleDetailView, ArticleByCategoryListView, articles_list


urlpatterns = [
    path('', ArcticleListView.as_view(), name='home'),
    path('articles/', articles_list, name='articles_by_page'),
    path('articles/<str:slug>/', ArticleDetailView.as_view(), name='articles_detail'),
    path('category/<str:slug>/', ArticleByCategoryListView.as_view(), name="articles_by_category"),
]