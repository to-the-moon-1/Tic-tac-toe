from django.shortcuts import render
from .func import *
from .models import Board
from .forms import BoardForm


def index(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        try:
            form.save()
        except:
            pass

    cells = Board.objects.all()

    my_board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

    for cell in cells:
        if not game_is_over(my_board):
            select_space(my_board, int(cell.value), "X")
            turn_o(my_board)
            if int(cell.value) == 0:
                my_board = [
                    ["1", "2", "3"],
                    ["4", "5", "6"],
                    ["7", "8", "9"]
                ]
                Board.objects.all().delete()
        elif int(cell.value) == 0:
            my_board = [
                ["1", "2", "3"],
                ["4", "5", "6"],
                ["7", "8", "9"]
            ]
            Board.objects.all().delete()
        else:
            pass

    over = game_is_over(my_board)

    context = {'board': my_board, 'over': over}

    return render(request, 'html/index.html', context)
