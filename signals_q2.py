from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def signal_handler(sender, instance, created, **kwargs):
    print("Signal thread:", threading.get_ident())

# Test code
if __name__ == "__main__":
    print("Main thread:", threading.get_ident())
    user = User.objects.create(username="testuser2")
