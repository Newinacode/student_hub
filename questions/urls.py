"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (QuestionListView,
                    QuestionDetailView,
                    QuestionCreateView,
                    QuestionUpdateView,
                    QuestionDeleteView)

urlpatterns = [
    path('', QuestionListView.as_view(), name='question_list'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('question/new/', QuestionCreateView.as_view(), name='question_create'),
    path('question/<int:pk>/update',
         QuestionUpdateView.as_view(), name='question_update'),
    path('question/<int:pk>/delete',
         QuestionDeleteView.as_view(), name='question_delete')

]
