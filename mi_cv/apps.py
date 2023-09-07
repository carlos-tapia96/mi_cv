from django.apps import AppConfig


class MiCvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mi_cv'

    def ready(self):
        import mi_cv.signals