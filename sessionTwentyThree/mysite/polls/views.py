from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.all()
    context = {'latest_question_list': latest_question_list}
    return render(request,'index.html',context)

def detail(request, question_id):
    """ return HttpResponse(f"You're looking at {question_id}") """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    """ response = f"you're looking at results of question {question_id}"
    return HttpResponse(response) """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")