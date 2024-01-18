from django.forms import ModelForm
from .models import Note, Tag
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError

class NoteForm(ModelForm):
  
  class Meta:
    model = Note
    fields = ['title', 'content', 'tags']
    
class TagForm(ModelForm):
  
  class Meta:
    model = Tag
    fields = ['tag_name']
    
  def clean_tag_name(self):
    tag_name = self.cleaned_data.get('tag_name')
    tag_name = ''.join([c for c in tag_name if not c.isspace()])
    if not tag_name.isalnum():
      raise ValidationError(_("Tag name should be alphanumeric"))
    return tag_name