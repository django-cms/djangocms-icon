# -*- coding: utf-8 -*-
from django import forms

from .fields import IconField
from .models import Icon


class IconForm(forms.ModelForm):
    icon = IconField(required=True)

    class Meta:
        model = Icon
        fields = ('label', 'icon', 'template', 'attributes',)

    def clean(self):
        self.cleaned_data['prefix'] = self.data.get('prefix')

    def save(self, commit=True):
        instance = super(IconForm, self).save(commit=False)
        instance.icon = "{} {}".format(self.cleaned_data['prefix'], self.cleaned_data['icon'])
        if commit:
            instance.save()
        return instance

