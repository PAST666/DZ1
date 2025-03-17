from django.apps import AppConfig


class CabinetConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cabinet"
    verbose_name = "Записи клиентов"

    def ready(self):
        import cabinet.signals
