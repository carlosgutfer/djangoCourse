from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect
from .models import Page
from .forms import PageForm

#Para que no se pueda editar todos los métodos de una clase 
class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        '''
        Hacer esto si por ejemplo quieres redirigir a otra cosa
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        '''
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm

    '''
    def get_success_url(self) -> str:
        return reverse('pages:pages')
        esto se puede cambiar por el método para vagos
    '''
    success_url = reverse_lazy('pages:pages')
    '''
    #Para evitar que un usuario sin permisos acceda a una pagina concreta
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(PageCreate, self).dispatch(request, *args, **kwargs)
    '''
@method_decorator(staff_member_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    fields = ['title', 'content', 'order']
    template_name_suffix = "_update_form"

    def get_success_url(self) -> str:
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'#esto lo hago para poder pasar mi objeto actualizado cuando guardo y recargo

@method_decorator(staff_member_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")