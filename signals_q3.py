from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class Dummy(models.Model):
    name = models.CharField(max_length=50)

@receiver(post_save, sender=Dummy)
def signal_handler(sender, instance, created, **kwargs):
    print("Inside signal, attempting rollback...")
    raise Exception("Forcing rollback")

# Test code
if __name__ == "__main__":
    try:
        with transaction.atomic():
            Dummy.objects.create(name="will_fail")
    except Exception as e:
        print("Transaction rolled back, nothing saved:", e)

    print("Objects count:", Dummy.objects.count())
