from django.conf.urls import url
from notes.models import Note
from . import views


urlpatterns = [
    url(r'^create-note/', views.NoteCreateView.as_view(model=Note, success_url='/')),
    url(r'^', views.NotesListView.as_view()),
]
