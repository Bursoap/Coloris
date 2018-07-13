from django.conf.urls import url
from notes.models import Note
from notes.views import NoteAPIView
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'note-api', NoteAPIView)

urlpatterns = [
    url(r'^create-note/', views.NoteCreateView.as_view(model=Note, success_url='/')),
    url(r'^$', views.NotesListView.as_view())
]

urlpatterns.extend(router.urls)
