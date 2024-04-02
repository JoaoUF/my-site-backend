from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models.CustomUser import CustomUser


@receiver(post_save, sender=CustomUser)
def show_email(sender, instance, **kwargs):
    print(instance.email)
