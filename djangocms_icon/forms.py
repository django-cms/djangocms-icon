# -*- coding: utf-8 -*-
from django import forms

from .fields import IconField
from .models import Icon


class IconForm(forms.ModelForm):
    icon = IconField(required=True)

    class Meta:
        model = Icon
        fields = ('label', 'icon', 'template', 'attributes',)
