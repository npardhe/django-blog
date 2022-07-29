#from .apiview import ApiView
from django.urls import path
from .views import HomeView,DetailView,AddPostView, UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,LikeView,AddCommentView,ApiView,ApiViewUserProfile,ApiViewUser,ApiViewComment
urlpatterns = [
    #path('', views.home,name="home"),
    path('',HomeView.as_view(),name="home"),
    path('article/<int:pk>',DetailView.as_view(),name="article-detail"),
    path('add_post',AddPostView.as_view(),name="add_post"),
    path('category/',AddCategoryView.as_view(),name='add_category'),
    path('article/edit/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(),name='delete_post'),
    path('category/<str:cats>',CategoryView,name='category'),
    path('category-list/',CategoryListView,name='category-list'),
    path('like/<int:pk>',LikeView,name='like_post'),
    path('article/<int:pk>/comment',AddCommentView.as_view(),name="add_comment"),
    path('api/',ApiView.as_view(),name='api'),
    path('api/profile/',ApiViewUserProfile.as_view(),name='apiprofile'),
    path('api/user/',ApiViewUser.as_view(),name='users'),
    path('api/comment/',ApiViewComment.as_view()),
    
   
]
