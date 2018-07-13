from django.db import models


class Note(models.Model):
    note_text = models.TextField(null=False, blank=False, max_length=2000)
    weight = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.note_text
