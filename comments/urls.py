from django.urls import path


from .views import CreateComment,CommentUpdateView,CommentDeleteView




urlpatterns =[
    path('comment/<int:pk>',CreateComment,name='create-comment'),
    path('comment/<int:pk>/update/',CommentUpdateView.as_view(),name='update-comment'),
    path('comment/<int:pk>/delete/',CommentDeleteView.as_view(),name='delete-comment'),
]


