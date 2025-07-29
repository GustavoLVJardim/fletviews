import flet as ft

def login_view(page, route):
    page.clean()
    
    def on_login_btn(e):

        if username_field.value and password_field.value:
            page.go(route)

        

    username_field: ft.TextField = ft.TextField(label="Username")
    password_field: ft.TextField = ft.TextField(label="Password", password=True, can_reveal_password=True)
    login_button: ft.ElevatedButton = ft.ElevatedButton("Login", on_click=on_login_btn)

    btn_home_view: ft.ElevatedButton = ft.ElevatedButton("Go Home",
    on_click=lambda e: page.go('/home')
    )

    page.add(btn_home_view, username_field, password_field, login_button,)
