import flet as ft
from controller.router import route

def main(page: ft.Page):
    page.title='fletviews'
    
    def handle_route_change(event):
        route(page, event.route) 

    page.on_route_change = handle_route_change
    page.go(page.route)

    

        


if __name__ == "__main__":
    ft.app(target=main)