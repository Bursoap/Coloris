from django.forms import Form
from notes.models import Note


class CreateNoteForm(Form):

    class Meta:
        model = Note
        fields = ('text',)
