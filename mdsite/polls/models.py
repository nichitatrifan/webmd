from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
import datetime

# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	summary = models.TextField(max_length=1000, help_text="Enter a brief description of the question", null = True)
	pub_date = models.DateTimeField('date published')

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	def __str__(self):
		return self.question_text

class Choice(models.Model):
	choice_text = models.CharField(max_length=200)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	votes = models.IntegerField(default=0)
	# user_id = models.BigIntegerField(null = True)

	def __str__(self):
		return self.choice_text