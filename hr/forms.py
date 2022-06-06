from tabnanny import verbose
from django import forms
from django.core.exceptions import ValidationError

from .models import Recruitment

class RecruitmentForm(forms.ModelForm):
    """ Form creation - Recruitment Form """
    
    class Meta:
        """ Recruitment Form Inherits from the Recruitment model. """

        model = Recruitment
        fields = [
            'dateOfRequest',
            'numberOfVacancies',
            'title']
        help_texts = {'requester': None,}
        verbose_name = [
            'Date of request',
            'Number of vacancies',
            'Title']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dateOfRequest'].widget.attrs.update({'class': 'form-control'})
        self.fields['numberOfVacancies'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'form-control'})