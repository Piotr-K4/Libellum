from .models import User, Profil
from django.db.models.signals import post_save, post_delete



def createProfile(sender,instance, created, **kwargs):
    if created:
        profile = Profil.objects.create(user=instance, username=instance.username)
        profile.save()


def deleteProfile(sender, instance, **kwargs):
    print("INSTANCJA", instance)






post_save.connect(createProfile, sender=User)
post_delete.connect(deleteProfile, sender=User)
