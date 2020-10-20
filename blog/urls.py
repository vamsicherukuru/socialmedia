from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('register',views.RegisterView,name='register'),
    path('logout',views.user_logout,name = 'logout'),
    path('login',views.user_login,name='user_login'),
    path('profile',views.profilePage.as_view(),name='profile'),
    path('news', views.NewsList.as_view(), name='news'),
    path('news/<int:pk>',views.NewsPostDetail.as_view(),name='news_detail'),
    path('newsPost',views.NewsNewPostView.as_view(),name='newsPost'),
    path('news/<int:pk>/comment',views.NewsAddComment.as_view(),name='NewsCommentAdd'),
    path('astroblog', views.AstroBlog.as_view(), name='astroblog'),
    path('post/<int:pk>',views.AstroPostDetail.as_view(),name='post_detail'),
    path('createPost',views.NewPostView.as_view(),name='createPost'),
    path('post/<int:pk>/comment',views.AddComment.as_view(),name='makeComment'),
    path('feedback',views.FeedbackView.as_view(),name='feedback'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)