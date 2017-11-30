from django import forms
from .models import Icon
from .fields import IconField


class IconForm(forms.ModelForm):
    class Meta:
        model = Icon
        fields = ('label', 'icon', 'template', 'attributes',)

    icon = IconField(required=True)
