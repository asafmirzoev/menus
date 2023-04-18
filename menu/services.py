from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Menu


def get_all_menu(request: HttpRequest) -> HttpResponse:
    menus = Menu.objects.all()
    return render(request, 'menu/menus.html', {'menus': menus})


def get_menu(request: HttpRequest, menu_id: int) -> HttpResponse:
    if (menu := Menu.objects.filter(pk=menu_id)).exists():
        return render(request, 'menu/menu.html', {'menu': menu.first()})

    messages.error(request, 'Меню не найдено')
    return redirect('menus')