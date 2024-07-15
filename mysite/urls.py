"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('accounts/', include('django.contrib.auth.urls')),  # Django authentication URLs
    path('blog/', include('blog.urls')),  # Blog app URLs
    path('profile/', views.my_profile, name='my_profile'),  # Redirect to logged-in user's profile
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login view
    path('profile/<str:adam1>/', views.profile, name='profile'),  # View other users' profiles
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Post detail view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
    path('', RedirectView.as_view(url='login/', permanent=False)),  # Redirect root to login
]