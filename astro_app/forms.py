from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Contact name',
            'email': 'Contact email',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'email'
            }),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
