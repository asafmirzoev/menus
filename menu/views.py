from django.views import View
from django.http import HttpRequest, HttpResponse

from . import services as svc


class MenusView(View):

    def get(self, request: HttpRequest, menu_id: int | None = None, ids: str | None = None) -> HttpResponse:
        if menu_id: return svc.get_menu(request, menu_id)
        return svc.get_all_menu(request)