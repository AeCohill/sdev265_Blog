from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Post model to represent a blog post
class Post(models.Model):
    # Author of the post, linked to the user model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Title of the post, limited to 200 characters
    title = models.CharField(max_length=200)
    # Text content of the post
    text = models.TextField()
    # Date and time when the post was created
    created_date = models.DateTimeField(default=timezone.now)
    # Date and time when the post was published
    published_date = models.DateTimeField(blank=True, null=True)

    # Method to publish the post, setting the published date to now
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # String representation of the Post model
    def __str__(self):
        return self.title
    
    # Method to get the author of the post
    def user(self):
        return self.author

    # Property to get the count of upvotes for the post
    @property
    def upvotes_count(self):
        return self.upvotes.count()

    # Property to get the count of downvotes for the post
    @property
    def downvotes_count(self):
        return self.downvotes.count()

# Upvote model to represent an upvote on a post
class Upvote(models.Model):
    # Post that is being upvoted, with a related name 'upvotes'
    post = models.ForeignKey(Post, related_name='upvotes', on_delete=models.CASCADE)
    # User who upvoted the post
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Date and time when the upvote was created
    created_date = models.DateTimeField(default=timezone.now)

    # Ensure that a user can upvote a post only once
    class Meta:
        unique_together = ('post', 'user')

# Downvote model to represent a downvote on a post
class Downvote(models.Model):
    # Post that is being downvoted, with a related name 'downvotes'
    post = models.ForeignKey(Post, related_name='downvotes', on_delete=models.CASCADE)
    # User who downvoted the post
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Date and time when the downvote was created
    created_date = models.DateTimeField(default=timezone.now)

    # Ensure that a user can downvote a post only once
    class Meta:
        unique_together = ('post', 'user')

# Profile model to represent user profiles
class Profile(models.Model):
    # User associated with the profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Profile picture of the user, with a default image and upload location
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    # String representation of the Profile model
    def __str__(self):
        return f'{self.user.username} Profile'
