import flet as ft
from views.login_view import login_view
from views.home_view import home_view
#from views.settings_view import settings_view

def route(page, route):
    page.clean()

    if route == "/" or route == "":
        page.go("/login")  # Redireciona para a tela de login

    elif route.startswith("/login"):
        login_view(page, route)
    elif route.startswith("/home"):
        home_view(page, route)
    #if route.startswith("/settings"):
     #   return settings_view(page, route)