
from django.contrib.auth.models import User
from .models import Profile

from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver


# Implimenting the signals
# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        #  Automatically create a profile when a user is created
        profile = Profile.objects.create(
            user=user,
            username = user.username,
            email = user.email,
            name = user.first_name,
            )

# @receiver(post_delete, sender=Profile)
def deleteUsers(sender, instance, **kwargs):
    # delete user when profile is deleted
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUsers, sender=Profile)
    