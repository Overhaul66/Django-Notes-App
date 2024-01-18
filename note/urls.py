from django.urls import path
from .views import HomeView, NoteCreateView, NoteDetailView, NoteUpdateView, NoteDeleteView
urlpatterns = [
  path('', HomeView.as_view() ,name='home'),
  path('note/create/', NoteCreateView.as_view(), name='create_note'),
  path('note/<slug:slug>/<int:pk>/', NoteDetailView.as_view(), name='note'),
  path('note/<slug:slug>/<int:pk>/update/', NoteUpdateView.as_view(), name='update'),
  path('note/delete/<slug:slug>/<int:pk>/', NoteDeleteView.as_view(), name='delete_note')
  ]