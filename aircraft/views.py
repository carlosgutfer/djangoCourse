from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import Aircraft

EXCLUDED_FIELDS = ('id', 'created', 'updated', 'name', 'manufacturer')

class AircraftListView(ListView):
    model = Aircraft
    template_name = 'aircraft/aircraft_list.html'
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

class AircraftCreateView(CreateView):
    model = Aircraft
    fields = [ 
    "name",
    "manufacturer",
    "model",
    "serial_number",
    "registration_number",
    "aircraft_type",
    "seating_capacity",
    "max_takeoff_weight",
    "empty_weight",
    "wingspan",
    "length",
    "height",
    "max_speed",
    "cruise_speed",
    "range_km",
    "fuel_capacity",
    "engine_type",
    "number_of_engines",
    "year_of_manufacture",
    "in_service"]
    success_url = reverse_lazy('aircrafts:list')

    def form_valid(self, form):
        instance = form.save()
        print("🟢 Avión guardado correctamente:", instance)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("❌ Formulario inválido:")
        print(form.errors)
        return super().form_invalid(form)