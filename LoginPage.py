from flet import Container, Image, TextButton, Button, Text, TextField, Colors,Column, Row, CrossAxisAlignment, MainAxisAlignment, alignment

imagemICON = Container(content=Image(src="./BOTICON.png"), width=180)
blue = "#1A388A"
 
def Loginpage(TextbuttonAction, entrarbuttonaction):
    
    textbutton = TextButton(text="Criar conta", scale=1.2)
    botaoentrar = Button(content=Text("Entrar", color=Colors.WHITE, size=20), height=60, width=480, bgcolor=blue, color=Colors.WHITE)
    
    pagina = Container(
        content=Column(
            controls=[imagemICON,
                      Text("Entrar", size=40, color=blue, weight="Bold"),
                      TextField(border_color=Colors.GREY,border_radius=15, label="Nome/E-mail", text_size=24, color=Colors.BLACK),
                      TextField(border_color=Colors.GREY,border_radius=15, label="Senha", text_size=24, color=Colors.BLACK, password=True, can_reveal_password=True),
                      botaoentrar,
                      Row(
                          controls=[Text("Não tem uma conta?", color=blue, size=20), textbutton],
                          alignment=MainAxisAlignment.CENTER)],
            spacing=15,
            horizontal_alignment=CrossAxisAlignment.CENTER
        ),
        alignment=alignment.center,
        padding=20,
    )
    textbutton.on_click = lambda e: TextbuttonAction(e)
    botaoentrar.on_click = lambda e: entrarbuttonaction(e)
    
    return pagina