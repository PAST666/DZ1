import re

from django import forms
from django.core.exceptions import ValidationError

from cabinet.models import Visit


class VisitModelForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ["name", "phone", "comment", "master", "services"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Ваше имя"}),
            "phone": forms.TextInput(
                attrs={
                    "type": "tel",
                    "placeholder": "Номер телефона (например, +79012345678)",
                }
            ),
            "comment": forms.Textarea(
                attrs={"placeholder": "Комментарий", "rows": 3}
            ),
            "master": forms.Select(),
            "services": forms.SelectMultiple(),
        }

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "").strip()
        phone_pattern = r"^(\+7|8)\d{10}$"
        if not re.match(phone_pattern, phone):
            raise ValidationError(
                "Номер телефона должен начинаться с +7 или 8 и "
                "содержать 10 цифр после кода (например, +79012345678)."
            )
        return phone
