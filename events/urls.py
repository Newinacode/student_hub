from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventListView.as_view(), name="event-list"),
    path('create/', views.EventCreateView.as_view(), name="event-create"),
    path('<pk>/delete/', views.EventDeleteView.as_view(), name="event-delete"),
    path("<pk>/detail/", views.EventDetailView.as_view(), name="event-detail"),
    path("<pk>/update/", views.EventUpdateView.as_view(), name="event-update"),
]
