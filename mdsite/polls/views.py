from django.shortcuts import render, redirect
from .models import Question, Choice 
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import F
from django.urls import reverse
from django.views import generic
from .forms import QuestionForm, AnswerForm
from django.contrib.auth.decorators import login_required

# Create your views here
 
class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		""" Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/vote.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        # was polls/detail.html
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
		})
    else:
    	selected_choice.votes = F('votes') + 1
    	selected_choice.save()
    	return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

@login_required
def create(request):
    # Создает новый вопрос в б/д
    error = ''
    # Проверяем, если использовался метод POST
    if request.method == 'POST':
        form = QuestionForm(request.POST) # В конструктор передаются все данные из формы
        # Являются ли данные корректо заполненными
        if form.is_valid():
            form.save()
            # Переадрессация
            return redirect('polls:create_answers')
        else:
            error = 'Форма неверна'
    form = QuestionForm()
    data = {
    'form':form,
    'error':error
    }

    return render(request, 'polls/create.html',data)

@login_required
def create_answers(request):
    error = ''
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:index')
        else:
            error = 'Форма неверна'
    form = AnswerForm()
    data = {
    'form':form,
    'error':error
    }
    return render(request, 'polls/create_answers.html',data)