
from django import forms

class FitFileUpload(forms.Form):
    """
    A Django form for uploading files.
    """
    fit_file = forms.FileField()