from django.urls import path

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('addarticle/', AddPage.as_view(), name='add_article'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('article/<slug:article_slug>/', ShowArticle.as_view(), name='article'),
    path('category/<slug:category_slug>/', PuzzleCategory.as_view(), name='category'),
    path('addlike/<int:pk>/', AddLike.as_view(), name='add_like'),
    path('favorite/', ShowFavorite.as_view(), name='favorite_show'),
    path('favorite/<int:pk>/', AddFavorite.as_view(), name='favorite'),
    path('addshare/', AddShare.as_view(), name='add_share'),
    path('share/', ShowShare.as_view(), name='share_show'),

]

