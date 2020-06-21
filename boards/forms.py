from django import forms
from boards.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        exclude = [
            'create_user',
        ]
