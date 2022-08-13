from django.db import models


class Board(models.Model):
    value = models.CharField(max_length=1)

    def __srt__(self):
        return self.value
