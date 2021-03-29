from django.db import models
from django.contrib.auth.models import User
# from urllib import request

# Create your models here.

class Post(models.Model):
	title = models.CharField('Title',max_length=150, default='Title')
	anons = models.CharField('Anons',max_length=250)
	full_text = models.TextField('Text')
	author = models.ForeignKey(User, on_delete = models.CASCADE,  null = True)
	date = models.DateTimeField('Date',auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return f'/posts/{self.id}'

	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'