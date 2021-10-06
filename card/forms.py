from django import forms
from .models import Card

from django.shortcuts import get_object_or_404
from django.http import Http404

class CardEditForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['profilepic', 'owner', 'name', 'position', 'company', 'website', 'mail', 'gsm', 'fax', 'instagramacc', 'twitteracc', 'linkedinacc']

class CardPPicForm(forms.ModelForm):
    class Meta:
        username = ""
        model = get_object_or_404(Card, owner = username)
        fields = ['profilepic']
