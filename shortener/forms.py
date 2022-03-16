from django import forms
from .models import Link
# import crispy_forms.bootstrap.

class LinkForm(forms.ModelForm):
    
    # ---- This works fine
    class Meta:
        model = Link
        fields = ['original_link']