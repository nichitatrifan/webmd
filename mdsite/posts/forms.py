from django import forms
from django.db import models
from .models import Post
# отдельно импортируем виджеты 
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select

class PostForm(ModelForm):
	class Meta:
		model = Post
		# fields = ['title','anons','full_text','date','author']
		fields = ['title','anons','full_text']

		widgets={
			"title":TextInput(attrs={'class':'form-control','placeholder':'Post Name'}),
			"anons":TextInput(attrs={'class':'form-control','placeholder':'Post Anons'}),
			"full_text":Textarea(attrs={'class':'form-control','placeholder':'Description'}),
			# "date":DateTimeInput(attrs={'class':'form-control','placeholder':'Date'})
		}