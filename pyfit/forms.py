
from django import forms

class FitFileUpload(forms.Form):
    """
    A Django form for uploading files.
    """
    export_csv = forms.BooleanField(required=False)
    fit_file = forms.FileField()