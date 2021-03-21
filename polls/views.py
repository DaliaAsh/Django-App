from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader
from django import forms
from datetime import datetime
from django.views.decorators.http import require_POST
from django.http import QueryDict
# Create your views here.


def index(request):
    if request.method == 'POST':
        addPoll(request)
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    all_polls_list = Question.objects.all()
    print(latest_question_list)
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
        'all_polls_list': all_polls_list
    }
    return render(request, 'polls/index.html', context)


def details(request, question_pk):
    if request.method == 'POST':
        addVote(request)
    question = get_object_or_404(Question, pk=question_pk)
    return render(request, 'polls/details.html', {'question': question})


def results(request, question_pk):
    return HttpResponse(f"You are looking at {question_pk} question results")


def votes(request, question_pk):
    return HttpResponse(f"You are looking at {question_pk} question votes")


@require_POST
def addPoll(request):
    question_text = QueryDict(request.body)['your_question']
    choices = QueryDict(request.body)['your_choices']
    new_question = Question(
        question_text=question_text,
        pub_date=datetime.now())
    new_question.save()
    choices_as_list = choices.split(',')
    for choice_text in choices_as_list:
        choice = Choice(question=new_question, choice_text=choice_text)
        choice.save()

    return redirect('index')


@require_POST
def addVote(request):
    id = QueryDict(request.body)['choice']
    chosen_choice = Choice.objects.get(pk=id)
    chosen_choice.votes = chosen_choice.votes + 1 
    chosen_choice.save()
    return redirect('index')