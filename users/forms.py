from django import forms
from django.contrib.auth.models import User
class UserRegistrForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'password')

    def save(self):
        super().save()
        user = User.objects.get(username=self.cleaned_data['username'])
        user.set_password(self.cleaned_data['password'])
        user.save()

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name')
