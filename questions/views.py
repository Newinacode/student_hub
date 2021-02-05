from django.shortcuts import render

# Create your views here.


def create_question(request):
    return render(request, 'questions/create_question.html')
