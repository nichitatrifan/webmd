from django import forms
from django.db import models
from .models import Question, Choice
# отдельно импортируем виджеты 
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, Select

class QuestionForm(ModelForm):
	class Meta:
		# указать фому
		model = Question
		# указать какие поля должны быть выведены
		fields = ['question_text','summary','pub_date']

		widgets = {
			"question_text":TextInput(attrs={'class':'form-control','placeholder':'Название вопроса'}),
			"summary":Textarea(attrs={'class':'form-control','placeholder':'Описание вопроса'}),
			"pub_date":DateTimeInput(attrs={'class':'form-control','placeholder':'Дата'})
		}

class AnswerForm(ModelForm):
	class Meta:
		model = Choice
		fields = ['question','choice_text']
		
		widgets = {
			"question":Select(attrs={'class':'form-control'}),
			"choice_text":TextInput(attrs={'class':'form-control','placeholder':'Название ответа'})
		}
		