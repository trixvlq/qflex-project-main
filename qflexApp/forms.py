from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Genre, Movie
class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username':forms.TextInput(attrs={'placeholder': 'username', 'style': 'width: 50%;', 'class': 'form-control'}),
            'first_name':forms.TextInput(attrs={'placeholder': 'first name', 'style': 'width: 50%;', 'class': 'form-control'}),
            'last_name':forms.TextInput(attrs={'placeholder': 'second name', 'style': 'width: 50%;', 'class': 'form-control'}),
            'email':forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 50%;', 'class': 'form-control'}),
            'password1':forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 50%;', 'class': 'form-control'}),
            'password2':forms.TextInput(attrs={'placeholder': 'email', 'style': 'width: 50%;', 'class': 'form-control'})
        }


class AddGenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('genreName', )

class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('__all__')