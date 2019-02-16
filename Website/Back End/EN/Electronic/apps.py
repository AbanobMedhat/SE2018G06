from django.apps import AppConfig


class ElectronicConfig(AppConfig):
    name = 'Electronic'

    def ready(self):
        import Electronic.signals
