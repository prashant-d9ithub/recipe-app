from django import forms
from .models import Recipe
from django.core import validators

class RecipeAdd(forms.ModelForm):
    
    class Meta:
        model = Recipe
        fields = ('rname','rcategory','rarea','rdrink','rinstruction')
        widgets = {
            'rname':forms.TextInput(attrs={'class':'form-control'}),
            'rcategory':forms.TextInput(attrs={'class':'form-control'}),
            'rarea':forms.TextInput(attrs={'class':'form-control'}),
            'rdrink':forms.TextInput(attrs={'class':'form-control'}),
            'rinstruction':forms.Textarea(attrs={'class':'form-control'}),
        }