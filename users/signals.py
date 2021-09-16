from django.db.models.signals import pre_save

from .models import User


def updateUser(sender, instance, **kwargs):
    print("ACIONOU")
    user = instance
    if user.email != "":
        user.username = user.email


pre_save.connect(updateUser, sender=User)
