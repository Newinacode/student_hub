from .forms import EventModelForm
from django.views import generic
from .models import Event

class EventCreateView(generic.CreateView): 
    template_name = 'events/create_event.html'
    form_class = EventModelForm


    def get_success_url(self):
        return reverse("list-event")


class EventDetailView(generic.DetailView):
    template_name = "events/event_detail.html"
    queryset = Event.objects.all()

    context_object_name = "event"


class EventUpdateView(generic.UpdateView): 
    template_name = "events/event_update.html"
    queryset = Event.objects.all()

    context_object_name = 'event'


class EventDeleteView(generic.DeleteView):
    template_name = "events/event_delete.html"
    queryset = Event.objects.all()



class EventListView(generic.ListView):
    template_name = "events/event_list.html"
    queryset = Event.objects.all()

    context_object_name = 'events'






