from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('posts/', views.post_list, name='post_list'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('Profile/', views.my_profile, name='my_profile'),  # Added this line
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('upvote/<int:post_id>/', views.upvote_post, name='upvote_post'),
    path('downvote/<int:post_id>/', views.downvote_post, name='downvote_post'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
