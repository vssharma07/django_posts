from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
	pass

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	published_date = models.DateField()
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title + ' | ' + str(self.author)

class Comment(models.Model):
	text = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(auto_now=True)
