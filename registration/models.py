from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

#metodo para borrar las imagenes antiguas de avatar
def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['user__username']

#Que crea un perfil enlazado a un usuario
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    #para que solo se lance cuando se crea una insatancia y no cuando se guarda
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)