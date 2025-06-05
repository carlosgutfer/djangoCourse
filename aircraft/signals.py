from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Aircraft
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def notify_aircraft_change(action, instance):
    print("📡 Notificando cambio:", action, instance.model)
    channel_layer = get_channel_layer()
    
    if channel_layer is None:
        print("❌ channel_layer es None — ver CHANNEL_LAYERS en settings.py")
        return

    print("📨 Enviando group_send")
    async_to_sync(channel_layer.group_send)(
        "aircraft_updates",
        {
            "type": "aircraft_event",
            "content": {
                "action": action,
                "aircraft": {
                    "id": instance.id,
                    "model": instance.model,
                    "manufacturer": instance.manufacturer,
                    "registration_number": instance.registration_number,
                }
            }
        }
    )


@receiver(post_save, sender=Aircraft)
def aircraft_saved(sender, instance, created, **kwargs):
    print("✅ SIGNAL aircraft_saved called")
    action = "created" if created else "updated"
    notify_aircraft_change(action, instance)

@receiver(post_delete, sender=Aircraft)
def aircraft_deleted(sender, instance, **kwargs):
    notify_aircraft_change("deleted", instance)
