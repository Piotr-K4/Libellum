from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.forms import ModelForm, widgets

# Create your models here.




class Profil(models.Model):
    sex = (
            ("Mężczyzna","Mężczyzna"),
            ("Kobieta","Kobieta"),
            )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, blank=False, null=True)
    profileImage = models.ImageField(upload_to="profiles/", default="profiles/user_default.png")
    dateBirth = models.DateField(default="1990-01-01")
    sexUser = models.CharField(choices=sex, default="Kobieta")
    description = models.TextField(max_length=500, blank=False, null=True)
    
    



    # @receiver(post_save, sender=User)
    # def create_profile(sender, instance, created , **kwargs):
    #     if created:
    #         Profil.objects.create(user=instance)

    def __str__(self):
        return self.user.username
