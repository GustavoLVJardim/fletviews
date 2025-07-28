import flet as ft

def login_view(page, route):
    page.clean()
    
    def on_login_btn(e):

        if username_field.value and password_field.value:
            page.go(route)

        login_button.on_click = on_login_btn

    username_field: type[TextField] = ft.TextField(label="Username")
    password_field: type[TextField] = ft.TextField(label="Password", password=True, can_reveal_password=True)
    login_button: ElevatedButton = ft.ElevatedButton("Login", on_click=on_login_btn)


