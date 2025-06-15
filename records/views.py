from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Record
from .forms import RecordForm

class RecordListView(LoginRequiredMixin, ListView):
    model = Record
    template_name = 'records/record_list.html'
    context_object_name = 'records'
    paginate_by = 10

class RecordCreateView(LoginRequiredMixin, CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'records/record_form.html'
    success_url = reverse_lazy('records:record_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Record
from .forms import RecordForm

class RecordListView(LoginRequiredMixin, ListView):
    model = Record
    template_name = 'records/record_list.html'
    context_object_name = 'records'
    paginate_by = 10

class RecordCreateView(LoginRequiredMixin, CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'records/record_form.html'
    success_url = reverse_lazy('records:record_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
