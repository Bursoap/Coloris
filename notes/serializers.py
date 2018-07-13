import re
from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ('note_text',)

    def create(self, validated_data):
        text = validated_data['note_text']
        weight = self.get_weight(text)
        note = Note.objects.create(note_text=text, weight=weight)
        return note

    def get_weight(self, text):
        word_list = re.sub('[-/:;()&@~#$%^*+=_|<>№,.?!]', "", text).lower().split()
        weight = 0
        for word in word_list:
            if word_list.count(word) > 1:
                continue
            weight += 1
        return weight
