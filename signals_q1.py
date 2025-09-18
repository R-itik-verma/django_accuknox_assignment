from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def signal_handler(sender, instance, created, **kwargs):
    print("Signal started...")
    time.sleep(5)
    print("Signal finished")

# Test code
if __name__ == "__main__":
    print("Creating user...")
    user = User.objects.create(username="testuser")
    print("User created")
