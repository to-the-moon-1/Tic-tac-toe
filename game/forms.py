from .models import Board
from django.forms import ModelForm


class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['value']
