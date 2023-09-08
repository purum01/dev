from django.contrib.auth.forms import UserCreationForm 
from django import forms 
from .models import Profile

class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    address = forms.CharField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', )

    def save(self):
        user = super().save() 
        Profile.objects.create(user=user, 
                               phone_number=self.cleaned_data['phone_number'],
                               address=self.cleaned_data['address'])
        return user