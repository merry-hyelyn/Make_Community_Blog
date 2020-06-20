from django.shortcuts import render, redirect, reverse
from boards.forms import BoardForm

# Create your views here.
def new(request):
    # board_form = BoardForm()
    # return render(request, "boards/new.html", {"board_form": board_form})
    return render(request, "boards/new.html")

