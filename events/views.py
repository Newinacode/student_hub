from .forms import EventModelForm
from django.views import generic
from .models import Event
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class EventCreateView(LoginRequiredMixin,generic.CreateView):
    template_name = 'events/event_update.html'
    form_class = EventModelForm
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def get_success_url(self):
        return reverse("event-list")

    


class EventDetailView(generic.DetailView):
    template_name = "events/event_detail.html"
    queryset = Event.objects.all()

    context_object_name = "event"


class EventUpdateView(generic.UpdateView):
    template_name = "events/event_update.html"
    model = Event
    fields = ('name','description','start_date','end_date' )

    context_object_name = 'event'




class EventDeleteView(generic.DeleteView):
    template_name = "events/event_delete.html"
    model = Event

    success_url = '/events/'


class EventListView(generic.ListView):
    template_name = "events/event_list.html"
    queryset = Event.objects.all()

    context_object_name = 'events'


    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     event = Event.objects.all()
    #     context ={
    #         "count" : event.count(),
    #         "rupesh_count" : len(event),
    #     }
    #     return context