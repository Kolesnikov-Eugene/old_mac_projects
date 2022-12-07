from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write your review here', widget=forms.Textarea(attrs={'class': 'myform',
#                                                                                                   'rows': '10'}))

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__" #pass all form from forms.py

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'stars': 'Rate'
        }

        error_messages = {
            'stars': {
                'min_value': 'min value is 1',
                'max_value': 'max value is 5'
            }
        }