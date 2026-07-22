from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Nome'), sg.Input(key='nome', size=(20,1))],
    [sg.Text ('Senha'),sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#janelas
janela = sg.Window('Tela de login', layout)
#Ler cadastro
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['nome'] == 'Felipe' and valores['senha'] == 'Felipe123':
            print('Bem vindo Felipe')