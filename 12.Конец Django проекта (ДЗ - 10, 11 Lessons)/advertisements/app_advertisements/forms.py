from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Advertisement
from django.core.exceptions import ValidationError


class AdvertisementForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['auction'].widget.attrs['class'] = 'form-check-input'
        self.fields['image'].widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Advertisement
        fields = ('title', 'description', 'price', 'auction', 'image')

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if title.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с ?')
        return title
        