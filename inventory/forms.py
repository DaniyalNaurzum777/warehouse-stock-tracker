from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "quantity", "min_quantity"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Мысалы: Кеңсе қағазы"}),
            "quantity": forms.NumberInput(attrs={"min": "0"}),
            "min_quantity": forms.NumberInput(attrs={"min": "0"}),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()
        if len(name) < 2:
            raise forms.ValidationError("Тауар атауы кемінде 2 таңбадан тұруы керек.")
        return name
