from flet import AlertDialog, Column, ListTile, Icon, Icons,Text

blue = "#1A388A"

def Menu(funcao):
    
    about = ListTile(
        leading=Icon(Icons.INFO, size=40),
        title=Text("Sobre", color=blue, size=25),
        on_click= lambda e: print("aba de sobre"),
        content_padding=10,
        tooltip="Sobre nós: Somos o grupo de empreendedorismo formado por Henderson, Diogo e Henrique Marques que trouxe uma solução para os serviços de atendimento, visando optar por substituir os bots por I.As adaptativas."
        
    )
    
    terms = ListTile(
        leading=Icon(Icons.PRIVACY_TIP, size=40),
        title=Text("Termos e política de privacidade", color=blue, size=25),
        on_click= lambda e: print("termos e politicas de privacidade"),
        content_padding=10,
        tooltip="Nao tem politica de privacidadeKKKKKKKKKKKKKKKKKKKK"
    )

    language = ListTile(
        leading=Icon(Icons.LANGUAGE, size=40),
        title=Text("Linguagem", color=blue, size=25),
        on_click= lambda e: print("escolher linguaguem"),
        content_padding=10,
        tooltip="Não tem outras linguas irmão, Aqui é Brazuca."
    )

    Tema = ListTile(
        leading=Icon(Icons.SUNNY, size=40),
        title=Text("Tema", color=blue, size=25),
        on_click= lambda e: print("escolher tema"),
        content_padding=10,
        tooltip="Vai ter que se contentar com o tema Claro, porque tô com preguiça."
    )
    
    acessibility = ListTile(
        leading=Icon(Icons.PEOPLE, size=40),
        title=Text("Acessibilidade", color=blue, size=25),
        on_click= lambda e: print("Aba de acessibilidade"),
        content_padding=10,
        tooltip="Isso aqui só roda em pc, só tem tema claro, não tem acessibilidade para gente cega, e precisa ter coordenação motora pra usar"
    )
    
    feedback = ListTile(
        leading=Icon(Icons.MAIL, size=40),
        title=Text("Feedback", color=blue, size=25),
        on_click= lambda e: print("Aba de feedback"),
        content_padding=10,
        tooltip="Enviar feedback."
    )
    
    sair = ListTile(
        leading=Icon(Icons.LOGIN, size=40),
        title=Text("Sair", color=blue, size=25),
        content_padding=10,
        tooltip="Sair da conta e voltar para a tela de login."
    )
    sair.on_click = lambda e: (funcao(e))

    
    aba = AlertDialog(
        content=Column(
            controls=[about,
                      terms,
                      language,
                      Tema,
                      acessibility,
                      feedback,
                      sair
                      ],
            spacing=0,
            width=1000
        )
    )
    return aba