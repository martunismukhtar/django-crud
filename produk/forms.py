from django import forms#, Textarea
from .models import Produk

class ProdukForm(forms.ModelForm):
    
    class Meta:
        model = Produk
        fields = "__all__"
        widgets = {
            'nama':forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            
        }