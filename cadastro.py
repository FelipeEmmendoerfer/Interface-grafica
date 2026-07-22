import json
from pathlib import Path
from PySimpleGUI import PySimpleGUI as sg

ARQUIVO_DADOS = Path(__file__).with_name('dados_login.json')


def carregar_dados():
    if ARQUIVO_DADOS.exists():
        try:
            with ARQUIVO_DADOS.open('r', encoding='utf-8') as arquivo:
                return json.load(arquivo)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def salvar_dados(dados):
    with ARQUIVO_DADOS.open('w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)


# Layout
sg.theme('Reddit')
dados_salvos = carregar_dados()

layout = [
    [sg.Text('Nome'), sg.Input(key='nome', size=(20, 1), default_text=dados_salvos.get('nome', ''))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1), default_text=dados_salvos.get('senha', ''))],
    [sg.Checkbox('Mostrar senha', key='mostrar_senha', enable_events=True)],
    [sg.Checkbox('Salvar o login?', key='salvar_login', default=dados_salvos.get('salvar_login', False))],
    [sg.Button('Entrar')]
]

# Janelas
janela = sg.Window('Tela de login', layout)

# Ler cadastro
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        dados_para_salvar = carregar_dados()
        dados_para_salvar['salvar_login'] = False
        salvar_dados(dados_para_salvar)
        break

    if eventos == 'Entrar':
        nome = valores['nome']
        senha = valores['senha']

        if nome == 'Felipe' and senha == '123456':
            print('Bem vindo Felipe!')
        elif nome == 'Thauany' and senha == '123456':
            print('Bem vinda Thauany!')
        else:
            print('Usuario ou senha incorretos')

        if valores['salvar_login']:
            salvar_dados({'nome': nome, 'senha': senha, 'salvar_login': True})
            print('Login salvo com sucesso!')
        else:
            salvar_dados({'nome': '', 'senha': '', 'salvar_login': False})

        janela.close()
        break
    if eventos == 'mostrar_senha':
        janela['senha'].update(password_char='' if valores['mostrar_senha'] else '*')
