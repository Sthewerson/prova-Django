from django.apps import AppConfig


class CursoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'curso'
    def ready(self):
        from curso import signals
