from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "light_stand_wms.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import light_stand_wms.users.signals  # noqa F401
        except ImportError:
            pass
