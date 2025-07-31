from django.apps import AppConfig


class AlunosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "students"

    def ready(self):
        import students.signals  # noqa: F401


