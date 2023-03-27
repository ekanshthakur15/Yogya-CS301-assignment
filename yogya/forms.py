from django import forms
from .models import Exhibit, Event, Talent, Review


class ExhibitForm(forms.ModelForm):
    class Meta:
        model = Exhibit
        fields = ['title', 'description',
                  'location']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description',
                  'location']


class TalentForm(forms.ModelForm):
    class Meta:
        model = Talent
        fields = ['name', 'contact_info']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
