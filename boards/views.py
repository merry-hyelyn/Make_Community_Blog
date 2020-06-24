from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, reverse
from boards.forms import BoardForm
from users.models import User


@user_passes_test(lambda u: u.is_staff or u.is_superuser, login_url="index")
def new(request):
    if request.method == "POST":
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board = board_form.save(commit=False)
            board.create_user = request.user
            board.save()
            return redirect('index')

    else:
        board_form = BoardForm()
        user = request.user
        return render(request, "boards/new.html", {
            "board_form": board_form,
            "user": user,
        })
