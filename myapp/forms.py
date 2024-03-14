from django import forms
from .models import Author


class AuthorForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()
    biography = forms.CharField(widget=forms.Textarea)
    data_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}
    ))


class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)
    # date = forms.DateTimeField()
    # author = forms.ModelChoiceField(queryset=Author.objects.all())
    is_published = forms.BooleanField()
    # views = forms.IntegerField()
