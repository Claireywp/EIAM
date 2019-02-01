import re
from django import forms
from django.core.exceptions import ValidationError

class sjk(forms.Form):
    Dname = forms.CharField