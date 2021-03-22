from django.urls import path
from .views import(
    NoteDetailView, NoteListView,
    NoteCreateView, NoteUpdateView
)

urlpatterns = [
    path('notes/', NoteListView.as_view(), name='note_list'),
    path('notes/create/', NoteCreateView.as_view(), name='note_create'),
    path('notes/<int:pk>/detail/', NoteDetailView.as_view(), name='note_detail'),
    path('notes/<int:pk>/update/', NoteUpdateView.as_view(), name='note_update'),

]
