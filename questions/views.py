from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.query_utils import Q
from django.http import request
from django.http.response import JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Question, Vote , QuestionView
from django.db.models import F



# Create your views here.

def visitor_ip_address(request):

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-date_posted']




class QuestionDetailView(DetailView):
    model = Question





    def get(self, request, *args, **kwargs):
        
        ip = visitor_ip_address(request)
        # print(ip)
        # print(request.META.get('HTTP_X_FORWARDED_FOR'))
        question = Question.objects.get(pk=kwargs['pk'])
        try:
            QuestionView.objects.get(IPAddress=ip,question=question)
        except:
            QuestionView.objects.create(IPAddress=ip,question=question)

            
        # print(request.headers) 
        return super().get(request)


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class QuestionUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Question
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False


class QuestionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Question
    success_url = '/'

    def test_func(self):
        question = self.get_object()
        if self.request.user == question.author:
            return True
        return False


def vote(request):
    if request.POST.get('action') == 'voting':
        id = int(request.POST.get('questionid'))
        button = request.POST.get('button')
        update = Question.objects.get(id=id)

        # New Selection
        if button == "upvote":
            update.votes = F('votes') + 1
            update.vote.add(request.user)
            update.save()

            # Add new vote
            new = Vote(question_id=id, user_id=request.user.id, vote=True)
            new.save()
        elif button == "downvote":
            update.votes = F('votes') - 1
            update.vote.add(request.user)
            update.save()

            # Add new vote
            new = Vote(question_id=id, user_id=request.user.id, vote=False)
            new.save()

        # Return updated Votes
        update.refresh_from_db()
        vote = update.votes

        return JsonResponse({'vote': vote})
