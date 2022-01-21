from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import DiscussionPost, Discreview


class DiscussionForm(ModelForm):
    class Meta:
        model = DiscussionPost
        fields = ['title','discription','body']

class ResponseForm(ModelForm):
    class Meta:
        model = Discreview
        fields = ['body']

        label = {
            'value':"Place your vote",
            'body': "Place your answer or response here"
        }