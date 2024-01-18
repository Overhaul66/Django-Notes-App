from django.contrib import admin
from .models import Note, Tag
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
  
  fieldsets = [
    ('Note', {'fields':['title','tags']}),
    ('Content', {'fields':['content']})
  ]
  
  list_display = [
    'title', 'date_created',
    ]
    
  list_filter = [
    'date_created', 'tags',
    ]
    
  search_fields = [
    'title',
    ]
    
admin.site.register(Note, NoteAdmin)