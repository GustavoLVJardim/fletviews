import flet as ft

def route(route,page_name):
    page.clean()

    if route.startswith("login"):
        return login_view(page_name)
    if route.startwith("home"):
        return home_view(page_name)
    if route.startwith("register"):
        return settings_view(page_name)