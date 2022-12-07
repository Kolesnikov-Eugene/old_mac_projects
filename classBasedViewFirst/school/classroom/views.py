from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from . import forms, models
from django.urls import reverse_lazy
from . import models


class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    model = models.Teacher
    # looks for model_form.html file in templates
    # .save()
    fields = '__all__'
    success_url = reverse_lazy('classroom:thank_you')


class ContactFormView(FormView):
    form_class = forms.ContactForm
    template_name = 'classroom/contact.html'
    success_url = reverse_lazy('classroom:thank_you')

    def form_valid(self, form):
        return super().form_valid(form)

class TeacherListView(ListView):
    # looks for model_list.html
    model = models.Teacher
    queryset = models.Teacher.objects.order_by('first_name')
    context_object_name = 'teacher_list'

class TeacherDetailView(DetailView):
    # RETURN ONLY ONE MODEL ENTRY PK
    # looks for model_detail.html
    model = models.Teacher
    # PK --> {{teacher}}

class TeacherUpdateView(UpdateView):
    # this view shares the model_form.html
    model = models.Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:teacher_list')

class TeacherDeleteView(DeleteView):
    # it's a form with a single "confirm delete" button
    # default trmplate name
    # model_confirm_delete.html
    model = models.Teacher
    success_url = reverse_lazy('classroom:teacher_list')