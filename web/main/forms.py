from django import forms
from django.core.validators import FileExtensionValidator

from main.models import Cars


class UploadFileForm(forms.Form):
    file = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=["csv"])]
    )
    car = forms.ModelChoiceField(queryset=Cars.objects.all())
