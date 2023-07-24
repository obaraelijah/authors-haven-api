from .celery import app as celery_app

# makes sure app is always imported when django starts so that shared taskw swll always use the app
__all__ = ("celery_app",)