from django import forms
from boards.models import Board


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        field = [
            "name",
            "create_user",
            "path",
        ]

        widget = {
            "name": forms.CharField(
                attrs={"class": "form-control", "placeholder": "15자 이내로 입력 가능합니다.",}
            ),
            "create_user": forms.EmailInput(attrs={"class": "form-control",}),
            "path": forms.CharField(
                attrs={
                    "class": "form-control",
                    "placeholder": "게시판 이름과 같은 경로이름을 권장합니다.",
                }
            ),
        }

        label = {
            "name": "게시판 이름",
            "create_user": "생성자",
            "path": "게시판 경로",
        }
