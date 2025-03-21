import re

from django import forms

from cabinet.models import Visit


class VisitModelForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ["name", "phone", "comment", "master", "services"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Ваше имя", "class": "form-control"}
            ),
            "phone": forms.TextInput(
                attrs={
                    "type": "tel",
                    "placeholder": "Номер телефона (Должен начинаеться с +7 или 8, длина 10 знаков!)",
                    "class": "form-control",
                }
            ),
            "comment": forms.Textarea(
                attrs={"placeholder": "Комментарий", "class": "form-control"}
            ),
            "master": forms.Select(attrs={"class": "form-control"}),
            "services": forms.SelectMultiple(attrs={"class": "form-control"}),
        }
        labels = {
            "master": "Врач",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Если форма содержит ошибки, добавляем класс 'is-invalid' к соответствующим полям
        for field_name, field in self.fields.items():
            if self.errors.get(field_name):
                widget_classes = field.widget.attrs.get("class", "")
                field.widget.attrs["class"] = f"{widget_classes} is-invalid"

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", "").strip()

        # Проверяем формат номера телефона: либо +7..., либо 8...
        phone_pattern = r"^(\+7|8)\d{10}$"
        if not re.match(phone_pattern, phone):
            raise forms.ValidationError(
                "Номер телефона должен начинаться с +7 или с 8 и содержать 10 цифр после кода страны."
            )

        return phone

    def clean(self):
        cleaned_data = super().clean()
        master = cleaned_data.get("master")
        selected_services = cleaned_data.get("services")

        if master and selected_services:
            # Получаем множество услуг, которые предоставляет мастер
            master_services = set(
                master.services.values_list("name", flat=True).distinct()
            )

            # Преобразуем услуги пользователя к множеству для сравнения
            selected_services_set = set(
                service.name for service in selected_services
            )

            # Приводим оба множества к нижнему регистру для страховки
            master_services = {service.lower() for service in master_services}
            selected_services_set = {
                service.lower() for service in selected_services_set
            }

            # Проверяем, что мастер предоставляет все выбранные услуги
            if not selected_services_set.issubset(master_services):
                # Вычисляем разность множеств, чтобы найти неподдерживаемые услуги
                unsupported_services = selected_services_set - master_services
                unsupported_services_str = ", ".join(unsupported_services)
                self.add_error(
                    "services",
                    f"Мастер {master.first_name} {master.last_name} "
                    f"не предоставляет следующие услуги: {unsupported_services_str}.",
                )

        return cleaned_data
