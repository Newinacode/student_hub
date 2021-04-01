from django.shortcuts import render
from .forms import CommentForm
# Create your views here.

from questions.models import Question
from .models import Comment
from django.views import generic


def CreateComment(request,pk):
    form = CommentForm(request.POST or None)
    context = {
        'form': form,
    } 

    if request.method == "POST":
        question = Question.objects.get(pk=pk)

        comment = Comment(user=request.user,content=form['content'],content_object=question)   
        comment.save()
        
        return render(request,'comments/com.html',context)



    return render(request,'comments/com.html',context)






class CommentUpdateView(generic.UpdateView):
    template_name = "events/event_update.html"
    model = Comment
    fields = ('content',)

    context_object_name = 'comment'




class CommentDeleteView(generic.DeleteView):
    template_name = "events/event_delete.html"
    model = Comment

    success_url = 'question-detail'