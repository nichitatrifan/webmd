from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

def posts_home(request):
	posts = Post.objects.order_by('-date')
	data = {
		'posts':posts,
	}
	return render(request,'posts/posts_home.html',data)

@login_required
def create_post(request):
	error=''
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.author = request.user
			instance.save()
			return redirect('posts:posts_home')
		else:
			error="Form is incorrect!!!"

	form = PostForm()
	data={
		'form':form,
		'error':error
	}
	return render(request,'posts/create_post.html',data)

class PostDetailView(DetailView):
	model = Post
	template_name = 'posts/post_details.html'
	context_object_name = 'post'

class PostUpdateView(UpdateView):
	model = Post
	template_name = 'posts/create_post.html'
	form_class = PostForm

class PostDeleteView(DeleteView):
	model = Post
	success_url = '/posts/'
	template_name = 'posts/delete_post.html'
	