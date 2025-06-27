from flet import Page, Container, AppBar, Row, IconButton, Icons, Text, MainAxisAlignment, ThemeMode, Colors, app

from LoginPage import Loginpage
from PaginadeEntrada import Paginaentrada
from RegisterPage import Registerpage
from Pagina_Chat import ChatPage
from menu import Menu

def main(page: Page):
    page.window.width = 480
    page.window.height = 800
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.padding = 0
    page.theme_mode = ThemeMode.LIGHT
    
    def entrartextbutton(e):
        _main_.content = loginpage
        page.close(menu)
        page.bottom_appbar.visible = False
        page.update()
    
    def Registrartextbutton(e):
        _main_.content = registerpage
        page.update()
    
    def Entrar_na_pagina_de_entrada(e):
        _main_.content = pagina_de_entrada
        page.update()
    
    def Entrar_no_chatbot(e):
        page.bottom_appbar.visible = True
        _main_.content = chatpage
        page.update()
    
    def back_page(e):
        if _main_.content == chatpage:
            _main_.content = pagina_de_entrada
        elif _main_.content == pagina_de_entrada:
            _main_.content = loginpage
        page.bottom_appbar.visible = False
        page.update()
        
    def menu_button(e):
        page.open(menu)
        page.update()
    
    pagina_de_entrada = Paginaentrada(Entrar_no_chatbot)    
    loginpage = Loginpage(Registrartextbutton, Entrar_na_pagina_de_entrada)
    registerpage = Registerpage(entrartextbutton, Entrar_na_pagina_de_entrada)
    chatpage = ChatPage(page)
    menu = Menu(entrartextbutton)
    page.drawer = menu
    
    blue = "#1A388A"
        
    page.appbar = AppBar(
        leading=Row(
            controls=[IconButton(icon=Icons.ARROW_BACK, icon_size=30, on_click=lambda e: back_page(e))],
            ),
        actions=[IconButton(icon=Icons.MENU, icon_size=30, on_click=lambda e: menu_button(e))],
        title=Text("Serviço de atendimento"),
        center_title=True,
        bgcolor=blue,
        color=Colors.WHITE,
        
    )
    
    _main_ = Container(
        expand=True
    )
    _main_.content = registerpage
    
    
    page.add(_main_)
    page.window.center()
    page.update()
app(target=main)