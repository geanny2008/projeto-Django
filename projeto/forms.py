from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.Aluno # parametros do models
        fields = '__all__' # fields dos campos

# importar os forms do jango e dos models ,, 