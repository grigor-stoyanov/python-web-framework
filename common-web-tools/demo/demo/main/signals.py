from django.dispatch import receiver
from django.db.models import signals
from demo.main.models import Profile

'''
Signals can be used for
Creating profile model for user
Send email after registration

Signals are fired automatically by  your view 
'''


@receiver(signals.pre_save, sender=Profile)
def profile_created(instance, **kwargs):
    print(f'pre create: {instance}')


@receiver(signals.post_save, sender=Profile)
def profile_created(instance, **kwargs):
    print(f'post create:{instance}')
