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
        labels = {
            'master': 'Врач',
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
    
    def clean(self):
        cleaned_data = super().clean()
        master = cleaned_data.get('master')
        selected_services = cleaned_data.get('services')

        if master and selected_services:
            # Получаем множество услуг, которые предоставляет мастер
            master_services = set(master.services.values_list('name', flat=True).distinct())
            
            # Преобразуем услуги пользователя к множеству для сравнения
            selected_services_set = set(service.name for service in selected_services)

            # Приводим оба множества к нижнему регистру для страховки
            master_services = {service.lower() for service in master_services}
            selected_services_set = {service.lower() for service in selected_services_set}
            
            # Проверяем, что мастер предоставляет все выбранные услуги
            if not selected_services_set.issubset(master_services):
                # Вычисляем разность множеств, чтобы найти неподдерживаемые услуги
                unsupported_services = selected_services_set - master_services
                unsupported_services_str = ', '.join(unsupported_services)
                self.add_error('services', f"Мастер {master.first_name} {master.last_name} не предоставляет следующие услуги: {unsupported_services_str}.")

        return cleaned_data
