from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

def qna_list(request):
    question_list = Question.objects.all()
    return render(request,'qna/list.html',{'question_list':question_list,})

def qna_detail(request, id):
    question = get_object_or_404(Question, id=id)
    form = QuestionForm(instance=question)
    answer_list = question.answer_set.all()
    return render(request,'qna/detail.html',{'form':form, 'answer_list':answer_list})

@login_required
def qna_add(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('qna:list')
    else:
        form = QuestionForm()
    return render(request, 'qna/question_form.html', {'form':form})

