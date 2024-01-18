from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Note
from .models import Tag
from .forms import NoteForm
# Create your views here.

class HomeView(ListView): 
  context_object_name = "notes"
  template_name = "note/home.html"
  
  def get_queryset(self):
    # sort notes from recent to latter
    return Note.objects.order_by('-date_created')
    
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['tags'] = Tag.objects.all()
    return context
    
class NoteDetailView(DetailView):
  model = Note
  template_name = "note/note.html"
  context_object_name = 'note'
    
class NoteCreateView(CreateView):
  model = Note
  form_class = NoteForm
  template_name = "note/create.html"
  
class NoteUpdateView(UpdateView):
  model = Note
  form_class = NoteForm
  template_name = "note/note_update_form.html"

class NoteDeleteView(DeleteView):
  model = Note
  success_url = reverse_lazy('home')
  template_name = "note/delete_note.html"
  