from django.shortcuts import render
from boards.models import Board
from posts.models import Post


def index(request, path=None):
    boards = Board.objects.all()
    posts = None

    if not path:
        path = "main"

    else:
        posts = Post.objects.filter(board__path=path)

    return render(
        request, "core/index.html", {"boards": boards, "path": path, "posts": posts}
    )

