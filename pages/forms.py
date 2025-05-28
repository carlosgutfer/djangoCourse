from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content','order' ]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-controls', 'placeholder': 'Titulo'}), 
            'content': forms.Textarea(attrs={'class':'form-controls'}),
            'order': forms.NumberInput(attrs={'class':'form-controls'}),
        }
        labels = {
            'title': '', 'order': '', 'content': ''
        }