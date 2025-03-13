import time
import random
import pyotp
from datetime import datetime
from colorama import Fore, Back, Style, init

# Inicializa o colorama para cores no terminal
init(autoreset=True)

# Variável global para armazenar o e-mail do usuário logado
usuario_logado = None

# Dicionário para armazenar os usuários
usuarios = {}

# Dicionário para armazenar os relacionamentos
relacionamentos = {}

# Dicionário para armazenar lembretes
lembretes = {}

# Dicionário para armazenar a linha do tempo
linha_do_tempo = {}

# Dicionário para armazenar metas e desafios
metas_desafios = {}

# Dicionário para armazenar perguntas e jogos
perguntas_jogos = {
    "perguntas": [
        "Qual foi o nosso primeiro encontro?",
        "Qual é a minha comida favorita?",
        "O que mais me faz feliz?",
        "Qual é o meu maior sonho?",
        "Qual é o meu filme preferido?"
    ],
    "jogos": [
        "Jogo da Verdade: Responda uma pergunta pessoal.",
        "Desafio do Abraço: Abrace-se por 1 minuto.",
        "Jogo do Elogio: Diga 3 coisas que ama no parceiro."
    ]
}

# Tabela de bodas
bodas_namoro = {
    1: "Bodas de Papel",
    2: "Bodas de Algodão",
    3: "Bodas de Couro",
    4: "Bodas de Flores",
    5: "Bodas de Madeira",
    6: "Bodas de Açúcar",
    7: "Bodas de Latão",
    8: "Bodas de Barro",
    9: "Bodas de Cerâmica",
    10: "Bodas de Estanho",
    15: "Bodas de Cristal",
    20: "Bodas de Porcelana",
    25: "Bodas de Prata",
    30: "Bodas de Pérola",
    40: "Bodas de Rubi",
    50: "Bodas de Ouro",
    60: "Bodas de Diamante"
}

bodas_casamento = {
    1: "Bodas de Papel",
    2: "Bodas de Algodão",
    3: "Bodas de Couro",
    4: "Bodas de Flores",
    5: "Bodas de Madeira",
    6: "Bodas de Açúcar",
    7: "Bodas de Latão",
    8: "Bodas de Barro",
    9: "Bodas de Cerâmica",
    10: "Bodas de Estanho",
    15: "Bodas de Cristal",
    20: "Bodas de Porcelana",
    25: "Bodas de Prata",
    30: "Bodas de Pérola",
    40: "Bodas de Rubi",
    50: "Bodas de Ouro",
    60: "Bodas de Diamante"
}

# Função para mostrar o coração 
def exibir_arte_ascii(titulo):
    print(Fore.RED + """
      ****     ****
    **    ** **    **
   **       **       **
  **                 **
  **                 **
   **               **
    **             **
     **           **
      **         **
       **       **
        **     **
         **   **
          ** **
           ***
            *
    """)
    print(Fore.YELLOW + titulo.center(40))
    print(Fore.RED + "=" * 40)

# função para validar e-mail
def validar_email(email):
    if email.count("@") != 1:
        return False
    if "." not in email.split("@")[1]:
        return False
    if " " in email:
        return False
    return True

# função para validar senha
def validar_senha(senha):
    if len(senha) != 8:
        return False
    if not any(char.isdigit() for char in senha):
        return False
    if not any(char.isupper() for char in senha):
        return False
    if " " in senha:
        return False
    return True

# função para gerar código de autenticação de dois fatores
def gerar_codigo_autenticacao():
    chave_mestra = pyotp.random_base32()
    totp = pyotp.TOTP(chave_mestra)
    return totp.now()

# função para cadastrar os usuário
def cadastrar_usuario():
    print(Fore.GREEN + "=====================================")
    print(Fore.GREEN + "===== ///// CADASTRO ///// =====")
    print(Fore.GREEN + "=====================================")
    email = input("Digite seu e-mail: ")
    if not validar_email(email):
        print(Fore.RED + "E-mail inválido!")
        return
    if email in usuarios:
        print(Fore.RED + "E-mail já cadastrado!")
        return
    senha = input("Digite sua senha (8 caracteres, 1 número, 1 maiúscula): ")
    if not validar_senha(senha):
        print(Fore.RED + "Senha inválida!")
        return
    usuarios[email] = {"senha": senha}
    print(Fore.GREEN + "Usuário cadastrado com sucesso!")

# função de listar os usuários
def listar_usuarios():
    print(Fore.GREEN + "=====================================")
    print(Fore.GREEN + "===== ///// USUÁRIOS CADASTRADOS ///// =====")
    print(Fore.GREEN + "=====================================")
    for email in usuarios:
        print(Fore.YELLOW + f"E-mail: {email}")

# função para atualizar senha
def atualizar_senha():
    global usuario_logado
    if not usuario_logado:
        print(Fore.RED + "Nenhum usuário logado!")
        return
    print(Fore.GREEN + "=====================================")
    print(Fore.GREEN + "===== ///// ATUALIZAR SENHA ///// =====")
    print(Fore.GREEN + "=====================================")
    senha_atual = input("Digite sua senha atual: ")
    if usuarios[usuario_logado]["senha"] != senha_atual:
        print(Fore.RED + "Senha atual incorreta!")
        return
    codigo_autenticacao = gerar_codigo_autenticacao()
    print(Fore.YELLOW + f"Seu código de autenticação é: {codigo_autenticacao}")
    codigo_digitado = input("Digite o código de autenticação: ")
    if codigo_digitado != codigo_autenticacao:
        print(Fore.RED + "Código de autenticação incorreto!")
        return
    nova_senha = input("Digite sua nova senha (8 caracteres, 1 número, 1 maiúscula): ")
    if not validar_senha(nova_senha):
        print(Fore.RED + "Senha inválida!")
        return
    usuarios[usuario_logado]["senha"] = nova_senha
    print(Fore.GREEN + "Senha atualizada com sucesso!")

# função para excluir usuário
def excluir_usuario():
    global usuario_logado
    if not usuario_logado:
        print(Fore.RED + "Nenhum usuário logado!")
        return
    print(Fore.GREEN + "=====================================")
    print(Fore.GREEN + "===== ///// EXCLUIR USUÁRIO ///// =====")
    print(Fore.GREEN + "=====================================")
    senha = input("Digite sua senha: ")
    if usuarios[usuario_logado]["senha"] != senha:
        print(Fore.RED + "Senha incorreta!")
        return
    del usuarios[usuario_logado]
    usuario_logado = None
    print(Fore.GREEN + "Usuário excluído com sucesso!")

# função para calcular tempo juntos
def calcular_tempo_juntos(data_inicio):
    hoje = datetime.now()
    diferenca = hoje - data_inicio
    anos = diferenca.days // 365
    meses = (diferenca.days % 365) // 30
    dias = (diferenca.days % 365) % 30
    return anos, meses, dias

# função de exibir tabela de bodas
def exibir_tabela_bodas(tipo):
    print(Fore.GREEN + "=====================================")
    print(Fore.GREEN + "===== ///// TABELA DE BODAS ///// =====")
    print(Fore.GREEN + "=====================================")
    tabela = bodas_namoro if tipo == "Namoro" else bodas_casamento
    for anos, nome in tabela.items():
        print(Fore.YELLOW + f"{anos} anos: {nome}")

# função para adicionar relacionamento
def adicionar_relacionamento():
    global usuario_logado
    if not usuario_logado:
        print(Fore.RED + "Nenhum usuário logado!")
        return
    print(Fore.GREEN + "=====================================")
    print(Fore.GREEN + "===== ///// ADICIONAR RELACIONAMENTO ///// =====")
    print(Fore.GREEN + "=====================================")
    tipo = input("Digite o tipo de relacionamento (Namoro, Noivado, Casamento): ")
    if tipo not in ["Namoro", "Noivado", "Casamento"]:
        print(Fore.RED + "Tipo de relacionamento inválido!")
        return
    data_inicio = input("Digite a data de início (AAAA-MM-DD): ")
    try:
        data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")
    except ValueError:
        print(Fore.RED + "Data inválida!")
        return
    relacionamentos[usuario_logado] = {"tipo": tipo, "data_inicio": data_inicio}
    print(Fore.GREEN + "Relacionamento adicionado com sucesso!")

# função de exibir tempo juntos
def exibir_tempo_juntos():
    global usuario_logado
    if not usuario_logado:
        print(Fore.RED + "Nenhum usuário logado!")
        return
    if usuario_logado not in relacionamentos:
        print(Fore.RED + "Relacionamento não encontrado!")
        return
    relacionamento = relacionamentos[usuario_logado]
    anos, meses, dias = calcular_tempo_juntos(relacionamento["data_inicio"])
    print(Fore.YELLOW + f"Tempo juntos: {anos} anos, {meses} meses, {dias} dias")
    exibir_arte_ascii(f"Bodas de {relacionamento['tipo']} - {anos} anos")

# função de adicionar lembrete
def adicionar_lembrete():
    global usuario_logado
    if not usuario_logado:
        print(Fore.RED + "Nenhum usuário logado!")
        return
    print(Fore.GREEN + "=====================================")
    print(Fore.GREEN + "===== ///// ADICIONAR LEMBRETE ///// =====")
    print(Fore.GREEN + "=====================================")
    data = input("Digite a data do lembrete (AAAA-MM-DD): ")
    try:
        data = datetime.strptime(data, "%Y-%m-%d")
    except ValueError:
        print(Fore.RED + "Data inválida!")
        return
    descricao = input("Digite a descrição do lembrete: ")
    if usuario_logado not in lembretes:
        lembretes[usuario_logado] = []
    lembretes[usuario_logado].append({"data": data, "descricao": descricao})
    print(Fore.GREEN + "Lembrete adicionado com sucesso!")

# Função para listar lembretes
def listar_lembretes():
    global usuario_logado
    if not usuario_logado:
        print(Fore.RED + "Nenhum usuário logado!")
        return
    if usuario_logado not in lembretes:
        print(Fore.RED + "Nenhum lembrete cadastrado!")
        return
    print(Fore.GREEN + "=====================================")
    print(Fore.GREEN + "===== ///// LEMBRETES ///// =====")
    print(Fore.GREEN + "=====================================")
    for lembrete in lembretes[usuario_logado]:
        print(Fore.YELLOW + f"Data: {lembrete['data'].strftime('%Y-%m-%d')} - Descrição: {lembrete['descricao']}")

# Função de adicionar marco na linha do tempo
def adicionar_marco():
    global usuario_logado
    if not usuario_logado:
        print(Fore.RED + "Nenhum usuário logado!")
        return
    print(Fore.GREEN + "=====================================")
    print(Fore.GREEN + "===== ///// ADICIONAR MARCO ///// =====")
    print(Fore.GREEN + "=====================================")
    data = input("Digite a data do marco (AAAA-MM-DD): ")
    try:
        data = datetime.strptime(data, "%Y-%m-%d")
    except ValueError:
        print(Fore.RED + "Data inválida!")
        return
    descricao = input("Digite a descrição do marco: ")
    if usuario_logado not in linha_do_tempo:
        linha_do_tempo[usuario_logado] = []
    linha_do_tempo[usuario_logado].append({"data": data, "descricao": descricao})
    print(Fore.GREEN + "Marco adicionado com sucesso!")

# Função para listar linha do tempo
def listar_linha_do_tempo():
    global usuario_logado
    if not usuario_logado:
        print(Fore.RED + "Nenhum usuário logado!")
        return
    if usuario_logado not in linha_do_tempo:
        print(Fore.RED + "Nenhum marco cadastrado!")
        return
    print(Fore.GREEN + "=====================================")
    print(Fore.GREEN + "===== ///// LINHA DO TEMPO ///// =====")
    print(Fore.GREEN + "=====================================")
    for marco in linha_do_tempo[usuario_logado]:
        print(Fore.YELLOW + f"Data: {marco['data'].strftime('%Y-%m-%d')} - Descrição: {marco['descricao']}")

# Função para adicionar meta / desafio
def adicionar_meta_desafio():
    global usuario_logado
    if not usuario_logado:
        print(Fore.RED + "Nenhum usuário logado!")
        return
    print(Fore.GREEN + "=====================================")
    print(Fore.GREEN + "===== ///// ADICIONAR META/DESAFIO ///// =====")
    print(Fore.GREEN + "=====================================")
    descricao = input("Digite a descrição da meta/desafio: ")
    if usuario_logado not in metas_desafios:
        metas_desafios[usuario_logado] = []
    metas_desafios[usuario_logado].append({"descricao": descricao, "concluido": False})
    print(Fore.GREEN + "Meta/Desafio adicionado com sucesso!")

# função para listar metas e desafios
def listar_metas_desafios():
    global usuario_logado
    if not usuario_logado:
        print(Fore.RED + "Nenhum usuário logado!")
        return
    if usuario_logado not in metas_desafios:
        print(Fore.RED + "Nenhuma meta/desafio cadastrado!")
        return
    print(Fore.GREEN + "=====================================")
    print(Fore.GREEN + "===== ///// METAS E DESAFIOS ///// =====")
    print(Fore.GREEN + "=====================================")
    for i, meta in enumerate(metas_desafios[usuario_logado]):
        status = "Concluído" if meta["concluido"] else "Pendente"
        print(Fore.YELLOW + f"{i + 1}. {meta['descricao']} - {status}")

# função do checklist nas metas
def marcar_concluido():
    global usuario_logado
    if not usuario_logado:
        print(Fore.RED + "Nenhum usuário logado!")
        return
    if usuario_logado not in metas_desafios:
        print(Fore.RED + "Nenhuma meta/desafio cadastrado!")
        return
    listar_metas_desafios()
    try:
        indice = int(input("Digite o número da meta/desafio que deseja marcar como concluído: ")) - 1
        if 0 <= indice < len(metas_desafios[usuario_logado]):
            metas_desafios[usuario_logado][indice]["concluido"] = True
            print(Fore.GREEN + "Meta/Desafio marcado como concluído!")
        else:
            print(Fore.RED + "Índice inválido!")
    except ValueError:
        print(Fore.RED + "Entrada inválida! Digite um número.")

# função para jogos e perguntas
def jogos_perguntas():
    global usuario_logado
    if not usuario_logado:
        print(Fore.RED + "Nenhum usuário logado!")
        return
    print(Fore.GREEN + "=====================================")
    print(Fore.GREEN + "===== ///// JOGOS E PERGUNTAS ///// =====")
    print(Fore.GREEN + "=====================================")
    print(Fore.YELLOW + "Escolha uma opção:")
    print(Fore.CYAN + "[1] Perguntas")
    print("[2] Jogos")
    opcao = input("Digite a opção: ")
    if opcao == "1":
        print(Fore.YELLOW + "\nPerguntas:")
        for pergunta in perguntas_jogos["perguntas"]:
            print(Fore.CYAN + f"- {pergunta}")
    elif opcao == "2":
        print(Fore.YELLOW + "\nJogos:")
        for jogo in perguntas_jogos["jogos"]:
            print(Fore.CYAN + f"- {jogo}")
    else:
        print(Fore.RED + "Opção inválida!")

# Menu interativo
def menu():
    global usuario_logado
    while True:
        print(Fore.BLUE + "=====================================")
        print(Fore.BLUE + "===== ///// BEM VINDO AO APP ///// =====")
        print(Fore.BLUE + "=====================================")
        print(Fore.CYAN + "[1] Cadastre-se e junte-se a nós")
        print("[2] Já se cadastrou? Faça o Login")
        print("[3] Sair do app")
        print(Fore.BLUE + "=====================================")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            print(Fore.GREEN + "=====================================")
            print(Fore.GREEN + "===== ///// LOGIN ///// =====")
            print(Fore.GREEN + "=====================================")
            email = input("Digite seu e-mail: ")
            if email not in usuarios:
                print(Fore.RED + "E-mail não encontrado!")
                continue
            senha = input("Digite sua senha: ")
            if usuarios[email]["senha"] != senha:
                print(Fore.RED + "Senha incorreta!")
                continue
            print(Fore.GREEN + "Login realizado com sucesso!")
            usuario_logado = email
            menu_logado()
        elif opcao == "3":
            print(Fore.RED + "Saindo...")
            break
        else:
            print(Fore.RED + "Opção inválida!")

# Menu após login
def menu_logado():
    global usuario_logado
    while True:
        print(Fore.BLUE + "=====================================")
        print(Fore.BLUE + "===== ///// MENU PRINCIPAL ///// =====")
        print(Fore.BLUE + "=====================================")
        print(Fore.CYAN + f"Usuário logado: {usuario_logado}")
        print(Fore.CYAN + "[1] Adicionar Relacionamento")
        print("[2] Exibir Tempo Juntos")
        print("[3] Exibir Tabela de Bodas")
        print("[4] Adicionar Lembrete")
        print("[5] Listar Lembretes")
        print("[6] Adicionar Marco na Linha do Tempo")
        print("[7] Listar Linha do Tempo")
        print("[8] Adicionar Meta/Desafio")
        print("[9] Listar Metas/Desafios")
        print("[10] Marcar Meta/Desafio como Concluído")
        print("[11] Jogos e Perguntas")
        print("[12] Atualizar Senha")
        print("[13] Logout")
        print("[14] Sair")
        print(Fore.BLUE + "=====================================")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_relacionamento()
        elif opcao == "2":
            exibir_tempo_juntos()
        elif opcao == "3":
            tipo = input("Digite o tipo de relacionamento (Namoro, Casamento): ")
            if tipo not in ["Namoro", "Casamento"]:
                print(Fore.RED + "Tipo de relacionamento inválido!")
            else:
                exibir_tabela_bodas(tipo)
        elif opcao == "4":
            adicionar_lembrete()
        elif opcao == "5":
            listar_lembretes()
        elif opcao == "6":
            adicionar_marco()
        elif opcao == "7":
            listar_linha_do_tempo()
        elif opcao == "8":
            adicionar_meta_desafio()
        elif opcao == "9":
            listar_metas_desafios()
        elif opcao == "10":
            marcar_concluido()
        elif opcao == "11":
            jogos_perguntas()
        elif opcao == "12":
            atualizar_senha()
        elif opcao == "13":
            usuario_logado = None
            print(Fore.GREEN + "Logout realizado com sucesso!")
            return
        elif opcao == "14":
            print(Fore.RED + "Saindo...")
            break
        else:
            print(Fore.RED + "Opção inválida!")

# Executa o menu
if __name__ == "__main__":
    exibir_arte_ascii("App do Casal")
    menu()