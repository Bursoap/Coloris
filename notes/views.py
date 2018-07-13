from django.views import generic
import re
from notes.forms import CreateNoteForm
from notes.models import Note


class NoteCreateView(generic.FormView):

    model = Note
    form_class = CreateNoteForm
    http_method_names = ('post',)

    def form_invalid(self, form):
        return super(NoteCreateView, self).form_invalid(form)

    def form_valid(self, form):
        text = form.data['note_text']
        weight = self.get_weight(text)
        Note.objects.create(note_text=text, weight=weight)
        return super(NoteCreateView, self).form_valid(form)

    def get_weight(self, text):
        word_list = re.sub('[-/:;()&@~#$%^*+=_|<>№,.?!]', "", text).lower().split()
        weight = 0
        for word in word_list:
            if word_list.count(word) > 1:
                continue
            weight += 1
        return weight


class NotesListView(generic.ListView):

    http_method_names = ('get',)
    model = Note
    template_name = 'notes/index.html'

    def get_queryset(self):
        return Note.objects.all().order_by('-weight')
