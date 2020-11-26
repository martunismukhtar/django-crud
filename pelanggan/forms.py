from django import forms#, Textarea
from .models import Pelanggan

class PelangganForm(forms.ModelForm):
    
    class Meta:
        model = Pelanggan
        fields = "__all__"
        # widgets = {
        #     'nama':forms.TextInput(
        #         attrs={
        #             "class": "form-control"
        #         }
        #     ),
        #     "alamat": forms.Textarea(
        #         attrs={
        #             "class": "form-control"
        #         }
        #     )
        # }