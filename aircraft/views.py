from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Aircraft

EXCLUDED_FIELDS = ('id', 'created', 'updated', 'name', 'manufacturer')

class AircraftListView(ListView):
    model = Aircraft
    template_name = 'aircrafts/aircraft_list.html'
    paginate_by = 10  # if pagination is desired

    def get_queryset(self):
        queryset = super().get_queryset()
        order_by = self.request.GET.get('sort', 'name')
        allowed_fields = [f.name for f in Aircraft._meta.fields if f.name not in EXCLUDED_FIELDS]
        if order_by.lstrip('-') in allowed_fields:
            return queryset.order_by(order_by)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['field_names'] = [field.verbose_name for field in Aircraft._meta.fields if field.name not in EXCLUDED_FIELDS]
        context['fields'] = [field.name for field in Aircraft._meta.fields if field.name not in EXCLUDED_FIELDS]
        context['current_sort'] = self.request.GET.get('sort', 'name')
        return context
# Create your views here.
