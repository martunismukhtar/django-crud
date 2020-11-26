from django import forms#, Textarea
from .models import Penerbit, Book

class PenerbitForm(forms.ModelForm):
    
    class Meta:
        model = Penerbit
        fields = "__all__"
        widgets = {
            'nama':forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "alamat": forms.Textarea(
                attrs={
                    "class": "form-control"
                }
            )
        }