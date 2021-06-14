from functools import wraps

from django.dispatch import receiver, Signal
from django.db.models.signals import pre_save, post_save, m2m_changed

from .models import *


def prevent_recursion(func):
    @wraps(func)
    def no_recursion(sender, instance=None, **kwargs):

        if not instance:
            return

        if hasattr(instance, '_dirty'):
            return

        func(sender, instance=instance, **kwargs)

        try:
            instance._dirty = True
            instance.save()
        finally:
            del instance._dirty

    return no_recursion
