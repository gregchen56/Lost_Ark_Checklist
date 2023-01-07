from django.urls import path
from .views import add_character_view, home_view

urlpatterns = [
    # ex: /lost_ark_checklist/
    path('', home_view, name="home"),
    path('add', add_character_view, name="add_char")
]