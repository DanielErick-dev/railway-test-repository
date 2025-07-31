from django.views import generic
from .models import Students
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from django.urls import reverse_lazy
from django.utils import timezone
from django.db.models import Q
from unidecode import unidecode
from django.shortcuts import redirect
from django.http import JsonResponse


class GetStudents(LoginRequiredMixin, generic.ListView):
    model = Students
    template_name = 'students/students.html'
    context_object_name = 'students'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name', '').strip()
        cpf = self.request.GET.get('cpf', '').strip()
        norm_name = unidecode(name).lower().replace(' ', '') if name else None
        norm_cpf = cpf.replace('-', '').replace('.', '') if cpf else None
        filters = Q()
        if norm_name:
            filters &= Q(name__icontains=norm_name) | Q(lastname__icontains=norm_name)
        if norm_cpf:
            filters &= Q(cpf__icontains=norm_cpf)
        return queryset.filter(filters).exclude(status='I')


class CreateStudents(LoginRequiredMixin, generic.CreateView):
    model = Students
    template_name = 'students/create_students.html'
    form_class = forms.StudentsForm
    success_url = reverse_lazy('get_students')

    def form_invalid(self, form):
        print('formulário inválido')
        print(form.errors)
        return super().form_invalid(form)


class DetailStudents(LoginRequiredMixin, generic.DetailView):
    model = Students
    template_name = 'students/detail_students.html'


class DeleteStudents(LoginRequiredMixin, generic.DeleteView):
    model = Students
    template_name = 'students/delete_students.html'
    success_url = reverse_lazy('get_students')

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            self.object = self.get_object()
            self.object.delete()
            return JsonResponse({'success': True})
        return super().post(request, *args, **kwargs)


class UpdateStudents(LoginRequiredMixin, generic.UpdateView):
    model = Students
    template_name = 'students/update_students.html'
    success_url = reverse_lazy('get_students')
    form_class = forms.StudentsForm


def atualize_students(request, pk):
    student = Students.objects.get(pk=pk)
    student.expiration_date = timezone.now().date() + timezone.timedelta(days=31)
    student.status = 'A'
    student.save()
    return redirect('get_students')


class GetPendingStudents(LoginRequiredMixin, generic.ListView):
    model = Students
    template_name = 'students/pending_students.html'
    context_object_name = 'pending_students'
    paginate_by = 10

    def get_queryset(self):
        pending_students = Students.objects.filter(status='P').order_by('last_status_change')
        return pending_students


class GetInactiveStudents(LoginRequiredMixin, generic.ListView):
    model = Students
    template_name = 'students/inactive_students.html'
    context_object_name = 'inactive_students'
    paginate_by = 10

    def get_queryset(self):
        inactive_students = Students.objects.filter(status='I')
        return inactive_students

