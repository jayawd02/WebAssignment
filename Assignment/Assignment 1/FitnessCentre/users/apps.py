from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
