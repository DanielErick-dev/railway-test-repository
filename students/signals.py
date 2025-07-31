from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Students
from django.utils import timezone


def atualize_expiration_date(instance):
    if not instance.created_at:
        instance.created_at = timezone.now()
    instance.expiration_date = instance.created_at + timezone.timedelta(days=31)
    instance.save()


@receiver(post_save, sender=Students)
def get_expiration_date(sender, instance, created, **kwargs):
    if created:
        atualize_expiration_date(instance)
