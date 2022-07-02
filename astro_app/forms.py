from django import forms
from .models import Reviews
# class ReviewsForm(forms.Form):
#     contact_name = forms.CharField(label='Contact name:', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     contact_email = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control',
#         'type': 'email'
#     }))
#     contact_message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'email', 'message']
        labels = {
            'name': 'Contact name',
            'email': 'Contact email',
        }
        # class = {
        #     'name': ''
        # }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'email'
            }),
            'message': forms.Textarea(attrs={'class': 'form-control'}),

        }