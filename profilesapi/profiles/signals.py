from django.contrib.auth.models import User
from django.db.models.signals import post_save  
from django.dispatch import receiver    
from profiles.models import Profile

"""
post_save signal that uses the User model as a sender to send a signal
every time a user instance is saved. So right after a user instance is saved
a signal is sent and the signal is going to be receievd by a function that
we're going to decorate with the receiver decorator import.

We're also going to know whether the user instance that has sent the signal 
if it has just been created or has just been modified.
"""

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    function with the receiver decorator. It knows to expect a signal sent by
    user so that in the context of the specific signal we're using 'post_save'.
    Right after a user instance has been saved the create_profile function 
    will be triggered. Due to the created parameter the function will know if
    it has to create a new profile instance or not.

    note - new step. Requires going to the __init__.py file and adding
    default_app_config parameter. Also requires goign to apps.py and adding
    a ready function that imports this signals.py file in its entirety.
    """
    print ('Created: ', created)
    if created:
        Profile.objects.create(user=instance)
