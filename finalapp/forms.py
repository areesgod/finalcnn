from dataclasses import fields
import imp
from pyexpat import model
from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = "__all__"