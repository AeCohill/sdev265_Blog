from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

# URL patterns for the application
urlpatterns = [
    # URL pattern for the login view
    path('login/', views.CustomLoginView.as_view(), name='login'),
    # URL pattern for the logout view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # URL pattern for the registration view
    path('register/', views.register, name='register'),
    # URL pattern for listing all posts
    path('posts/', views.post_list, name='post_list'),
    # URL pattern for displaying a user's profile
    path('profile/<str:username>/', views.profile, name='profile'),
    # URL pattern for redirecting to the logged-in user's profile
    path('Profile/', views.my_profile, name='my_profile'),  # Added this line
    # URL pattern for displaying an author's details and their posts
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    # URL pattern for upvoting a post
    path('upvote/<int:post_id>/', views.upvote_post, name='upvote_post'),
    # URL pattern for downvoting a post
    path('downvote/<int:post_id>/', views.downvote_post, name='downvote_post'),
    # URL pattern for creating a new post
    path('post/new/', views.post_new, name='post_new'),
    # URL pattern for editing an existing post
    path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
]

# If in DEBUG mode, serve media files through Django
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
