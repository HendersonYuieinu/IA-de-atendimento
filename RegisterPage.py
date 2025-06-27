from flet import Container, Image, Text, TextField, Colors, Button, TextButton,Column, Row, CrossAxisAlignment, MainAxisAlignment, alignment


imagemICON = Container(content=Image(src="./BOTICON.png"), width=180)
blue = "#1A388A"
 
def Registerpage(textbuttonaction, registrarbuttonaction):
    
    textbutton = TextButton(text="Entrar", scale=1.2)
    registarbutton = Button(content=Text("Registrar", color=Colors.WHITE, size=20), height=60, width=480, bgcolor=blue, color=Colors.WHITE,)
    
    pagina = Container(
        content=Column(
            controls=[imagemICON,
                      Text("Criar conta", size=40, color=blue, weight="Bold"),
                      TextField(border_color=Colors.GREY,border_radius=15, label="Nome", text_size=24, color=Colors.BLACK),
                      TextField(border_color=Colors.GREY,border_radius=15, label="E-mail", text_size=24, color=Colors.BLACK),
                      TextField(border_color=Colors.GREY,border_radius=15, label="Senha", text_size=24, color=Colors.BLACK, password=True, can_reveal_password=True),
                      registarbutton,
                      Row(
                          controls=[Text("Já tem uma conta?", color=blue, size=20), textbutton],
                          alignment=MainAxisAlignment.CENTER)],
            spacing=15,
            horizontal_alignment=CrossAxisAlignment.CENTER
        ),
        alignment=alignment.center,
        padding=20
    )
    textbutton.on_click = lambda e: textbuttonaction(e)
    registarbutton.on_click = lambda e: registrarbuttonaction(e)
    
    return pagina
