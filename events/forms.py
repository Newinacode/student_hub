from django import forms 
from .models import Event





class EventModelForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name','description','start_date','end_date' )
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }