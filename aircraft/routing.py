from django.urls import re_path
from aircraft.consumers import AircraftConsumer

websocket_urlpatterns = [
    re_path(r'^ws/aircrafts/$', AircraftConsumer.as_asgi()),
    ]