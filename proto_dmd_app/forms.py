from django import forms
from django.forms import ModelForm
from .models import MarkdownContent

class MarkdownForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'})
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'w-full px-3 py-2 border rounded-lg', 'rows': 10})
    )
    slug = forms.SlugField(
        widget=forms.TextInput(attrs={'class': 'w-full px-3 py-2 border rounded-lg'})
    )

    class Meta:
        model = MarkdownContent
        fields = '__all__'
