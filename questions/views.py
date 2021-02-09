from django.shortcuts import render

# Create your views here.


def question_list(request):
    return render(request, 'index.html')


def create_question(request):
    return render(request, 'questions/create_question.html')
