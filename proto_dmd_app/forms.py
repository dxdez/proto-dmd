from django.forms import ModelForm
from .models import MarkdownContent

class MarkdownForm(ModelForm):
    class Meta:
        model = MarkdownContent
        fields = '__all__'
