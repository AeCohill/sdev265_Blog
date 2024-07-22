from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Upvote, Downvote
from django.contrib.auth import login, authenticate
from .forms import PostForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# View to list all posts
def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/post_list.html', context)

# View to display the details of a specific post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# Custom login view that redirects authenticated users
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

# View to handle user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('post_list')
        else:
            print(form.errors)  # Debugging: print form errors
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# View to render the home page, checking if the user is authenticated
def home(request, user):
    if User.is_authenticated:
        return render(request, 'blog/post_list.html')
    else:
        return render(request, 'registration/login.html')

# View to display details of a specific author and their posts
def author_detail(request, pk):
    author = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author=author)
    context = {
        'author': author,
        'posts': posts
    }
    return render(request, 'blog/author_detail.html', context)

# View to handle upvoting a post
def upvote_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if not Upvote.objects.filter(post=post, user=request.user).exists():
        Upvote.objects.create(post=post, user=request.user)
    return redirect('post_list')

# View to handle downvoting a post
def downvote_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if not Downvote.objects.filter(post=post, user=request.user).exists():
        Downvote.objects.create(post=post, user=request.user)
    return redirect('post_list')

# View to create a new post
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# View to edit an existing post
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

# View to redirect to the profile page of the logged-in user
@login_required
def my_profile(request):
    return redirect('profile', username=request.user.username)

# View to display a user's profile and their posts
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user)
    context = {
        'profile_user': user,
        'posts': posts
    }
    return render(request, 'blog/profile.html', context)

# View to delete a post
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
