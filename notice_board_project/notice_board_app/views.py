# notice_board_app/views.py

from django.shortcuts import render

def message_page(request):
    return render(request, 'message_page.html')

def display_page(request):
    return render(request, 'display_page.html')
