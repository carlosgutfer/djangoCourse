from django.urls import path
from .views import AircraftListView, AircraftCreateView

aircrafts_patterns = ([
    path('', AircraftListView.as_view(), name='list'),
    path('create/', AircraftCreateView.as_view(), name='create'),
], "aircrafts")