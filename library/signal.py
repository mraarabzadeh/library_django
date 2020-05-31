from django.db.models.signals import pre_save
from django.dispatch import receiver
from library.models import Book


def send_email(address, book):
    pass


@receiver(pre_save, sender=Book)
def email_sender(sender, **kwargs):
    pass
    # for item in sender.instance:
    #     send_email(item, item)
