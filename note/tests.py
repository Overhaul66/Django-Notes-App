from django.test import TestCase
from django.urls import reverse
from .models import Note
from django.utils.text import slugify
# Create your tests here.

def create_note(note_title, note_content):
  return Note.objects.create(title = note_title, content = note_content)

class IndexViewTest(TestCase):
  
  def test_no_notes(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "There are no notes")
    self.assertQuerySetEqual(response.context['notes'], [])
  
  #test if the note shows 
  def test_home_notes_view(self):
    note = create_note( "A test title","A test content")
    response = self.client.get(reverse('home'))
    # test if response was successful
    self.assertEqual(response.status_code, 200)
    #self.assertContains(response, 'A test title')
    # test queryset
    self.assertQuerySetEqual(response.context['notes'], [note], )
    
  def test_home_multiple_notes_view(self):
    note1 = create_note("A test for note1","A content for note1")
    note2 = create_note("A test for note2","A content for note2")
    note3 = create_note('A test for note3', 'A content for note3')
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    #also confirms notes displays according to recent date
    self.assertQuerySetEqual(response.context['notes'], [note3, note2, note1])
class NoteDetailViewTest(TestCase):
  
  def test_note_object_detail_view(self):
    note = create_note('a title', 'a content')
    response = self.client.get(reverse('note',
    kwargs = {
      'slug' : note.slug,
      'pk' : note.pk,
    }))
    
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "a title")
    self.assertContains(response, 'a content')
    
  def test_no_note_object_detail_view(self):
    response = self.client.get(
      reverse('note', 
      kwargs = {
        'slug' : 1,
        'pk' : 1,
      })
      )
      
    self.assertEqual(response.status_code, 404)
class NoteCreateViewTest(TestCase):
  
  def test_note_creation(self):
    url = reverse('create_note')
    response = self.client.post(
      url, {
        'title':'a title',
        'content':'a content'
        }
    )
    
    #check if there is a redirect
    self.assertEqual(response.status_code, 302)
    obj_slug = slugify('a title')
    self.assertRedirects(response, reverse('note', kwargs = {'slug':obj_slug, 'pk':1}))
    #check if objects exists in database
    note_object = Note.objects.get(title="a title")
    self.assertIsNotNone(note_object)
class NoteUpdateViewTest(TestCase):
  
  def test_note_update(self):
    note = create_note('note_title', 'note content')
    url = reverse("update", kwargs = {
      'slug':slugify(note.title),
      'pk':1
    })
    
    updated_note = {
      "title":"updated title",
      "content":"updated content"
    }
    
    response = self.client.post(url, updated_note)
    
    self.assertEqual(response.status_code, 302)
    slug = slugify(updated_note['title'])
    expected_url = reverse('note', 
    kwargs = {
      'slug':slug,
      'pk':1
    })
    self.assertRedirects(response, expected_url
    )
    # test if the object was updated
    updated_note = Note.objects.get(pk=1)
    self.assertEqual(updated_note.title, "updated title")
    self.assertEqual(updated_note.content, "updated content")