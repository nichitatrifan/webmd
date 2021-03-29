from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from .forms import RegisterForm

# Create your views here.
class RegisterView(FormView):
	template_name = 'registration/register.html'
	form_class = RegisterForm
	success_url = 'polls:index'

	def form_valid(self, form):
		form.save()
		return redirect('polls:index')
