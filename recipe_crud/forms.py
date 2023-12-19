from django.core import validators
from django import forms
from .models import Recipe

class RecipeAdd(forms.ModelForm):
  
    class Meta:
        model = Recipe
        fields = ('rname', 'rcategory', 'rarea', 'rdrink', 'rinstruction', 'rvideoLink')
        widgets = {
            'rname': forms.TextInput(attrs={'class': 'form-control'}),
            'rcategory': forms.TextInput(attrs={'class': 'form-control'}),
            'rarea': forms.TextInput(attrs={'class': 'form-control'}),
            'rdrink': forms.TextInput(attrs={'class': 'form-control'}),
            'rinstruction': forms.Textarea(attrs={'class': 'form-control'}),
            'rvideoLink': forms.URLInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'rname': 'Recipe Name',
            'rcategory': 'Recipe Category',
            'rarea': 'Recipe Area',
            'rdrink': 'Recipe Drink',
            'rinstruction': 'Recipe Instructions',
            'rvideoLink': 'Recipe VideoLink',
        }
    def __init__(self, *args, **kwargs):
        super(RecipeAdd, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            print(f'field : {field} || field_name: {field_name}')
            field.label_suffix = ' '
