from flet import Container, VerticalAlignment, Image, Row, Column, Text, Colors, Icon, Icons, BoxShadow, Offset, TextAlign, CrossAxisAlignment, MainAxisAlignment, TextField, IconButton, BottomAppBar, ListView, margin
from chatScript import enviar_mensage


imagemICON = Container(content=Image(src="./BallerinaCappuccina.png"), width=60)
blue = "#1A388A"

def mensage_AI(msg):

    mensagem = Container(
        content=Row(
            controls=[imagemICON, Column(controls=[
                                                             Text("Assistente I.A", size=14, color=blue, weight='Bold'),
                                                             Text(msg, size=16, width=250, no_wrap=False, text_align=TextAlign.JUSTIFY)       
                                                            ]
                                                            
            )],
            vertical_alignment=VerticalAlignment.START
        ),
        bgcolor=Colors.BLUE_GREY_100,
        padding=10,
        border_radius=10,
        margin=margin.only(right=100),
        shadow=BoxShadow(0.01, 5, Colors.BLACK, offset=Offset(x=0, y=2))
    )
    return mensagem

def sendMensagem(e, page, listview, mensagem_textfield, texto):
    listview.controls.append(mensage_USER(mensagem_textfield.value))
    mensagem_textfield.value = ""
    page.update()
    
    resposta = enviar_mensage(texto)
    listview.controls.append(mensage_AI(resposta))
    page.update()

def mensage_USER(msg):
    mensagem = Container(
        content=Row(
            controls=[
                Column(controls=[
                                    Text("Usuario", size=14, color=Colors.WHITE, weight='Bold', text_align=TextAlign.RIGHT),
                                    Text(msg, size=16, width=250, no_wrap=False, color=Colors.WHITE, text_align=TextAlign.JUSTIFY)       
                                    ],
                                horizontal_alignment=CrossAxisAlignment.END
                                ),
                Icon(Icons.PERSON, size=60, color=Colors.WHITE)],
            alignment=MainAxisAlignment.END,
        ),
        bgcolor=Colors.BLUE_900,
        padding=10,
        border_radius=10,
        margin=margin.only(left=100),
        shadow=BoxShadow(0.01, 5, Colors.BLACK, offset=Offset(x=0, y=2))
    )
    return mensagem

 
def ChatPage(page):
    mensagem_textfield = TextField(expand=True, multiline=True, hint_text="Digite aqui", border_width=0, text_size=20)    
    enviar_mensagem_button = IconButton(Icons.SEND, icon_size=40)
    page.bottom_appbar = BottomAppBar(
                content=Row(
                    controls=[mensagem_textfield, enviar_mensagem_button],
                    alignment=MainAxisAlignment.END
                ),
                visible=False)
    listview = ListView(
            controls=[mensage_AI("Olá, como posso ajudar?")],
            spacing=15,
            padding=10
        )
    pagina = Container(
        content=listview
    )
        
    enviar_mensagem_button.on_click = lambda e: (sendMensagem(e, page, listview, mensagem_textfield, mensagem_textfield.value))

    return pagina
