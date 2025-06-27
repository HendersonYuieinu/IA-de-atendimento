from flet import app, Container, Image, Column, Text, CrossAxisAlignment,Colors, Button, alignment, ListTile, Icon, Icons, Card,RoundedRectangleBorder



def create_card(atividade, time):
    card = Card(
        ListTile(leading=Icon(Icons.CHAT, color=blue),
                    title=Text(f'{atividade}', color=blue, weight="Bold"),
                    subtitle=Text(f'{time} dias atrás', color=blue, italic=True),
                    on_click=lambda e: print("opened")),
        expand=True,
        color=Colors.WHITE,
        elevation=2,
        shadow_color=Colors.ON_SURFACE_VARIANT,
        shape=RoundedRectangleBorder(radius=10),
        )
    return card

imagemICON = Container(content=Image(src="./BOTICON.png"), width=180)
blue = "#1A388A"

texto = Column(controls=[Text("Bem-vindo ao Suporte!", size=30, color=blue, weight="Bold"),
                            Text("Pergunte algo ou descreva seu problema.", size=15, color=blue),],
                  spacing=0,
                  horizontal_alignment = CrossAxisAlignment.CENTER)

atividaderecente = Column(
    controls=[Text("Atividade Recente", size=20, color=blue, weight="Bold")],
    spacing=2
)

for time in range(4):
    atividaderecente.controls.append(create_card("<atividade>", time+1))
 
def Paginaentrada(botao_action):
    button = Button(content=Text("Iniciar conversa", color=Colors.WHITE, size=20), height=60, width=480, bgcolor=blue, color=Colors.WHITE,)
    
    pagina = Container(
        content=Column(
            controls=[imagemICON,
                      texto,
                      button,  
                      atividaderecente],
            spacing=40,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            scroll=True
        ),
        alignment=alignment.center,
        padding=20
    )
    button.on_click = lambda e: botao_action(e)
    
    return pagina