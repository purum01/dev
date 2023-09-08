from django.urls import path
from django.urls.base import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from . import views
from .models import Question, Answer
from .forms import QuestionForm

app_name = 'qna'
urlpatterns = [
    path('add/', views.qna_add, name='add'),
    path('<pk>/update/', UpdateView.as_view(model=Question, form_class=QuestionForm), name='update'),
    path('<pk>/delete/', DeleteView.as_view(model=Question, success_url=reverse_lazy('qna:list')), name='remove'),
    path('', views.qna_list, name='list'),
    path('<id>/', views.qna_detail, name='detail'),
]