from django.urls import path
from .views import AircraftListView

aircrafts_patterns = ([
    path('', AircraftListView.as_view(), name='list'),
], "aircrafts")