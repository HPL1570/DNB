from django import forms
from .models import StoreImages

class StoreImagesForm(forms.ModelForm):
    class Meta:
        model = StoreImages
        fields = ['name','image']