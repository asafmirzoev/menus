from django.urls import path

from .views import MenusView

urlpatterns = [
    path('', MenusView.as_view(), name='menus'),
    path('<int:menu_id>/', MenusView.as_view(), name='menus'),
    path('<int:menu_id>/<str:ids>/', MenusView.as_view(), name='menus'),
]