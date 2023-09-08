from django.db import models
from django.conf import settings
from django.urls import reverse
from shop.models import Product

class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(verbose_name='질문')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
  
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("qna:detail", kwargs={"id": self.id})
    

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='답변')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content