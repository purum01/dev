from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'updated_at', 'status']
    search_fields = ['status']

    inlines = (AnswerInline,)



@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['content','question', 'question_id', 'created_at', 'updated_at']

    