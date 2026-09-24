import os, time
lista_alunos = []

def cadastro_aluno():
    while True:
        
        nome_aluno = input("Qual é o nome do aluno? ").strip()
        while True:
            try:
                nota_aluno = float(input(f"Qual é a nota do Aluno(a) {nome_aluno}? "))
                break
            except ValueError:
                print("Erro! digite apenas números (ex. 8.5). Tente novamente")
        
        if nome_aluno:
            lista_alunos.append({"nome": nome_aluno, "nota": nota_aluno})
            print(f"O aluno {nome_aluno} foi cadastrado com sucesso!")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("O campo não pode ficar vazio. tente novamente")

def listar_alunos():
    print("---- Alunos cadastrados na escola: ----")
    for aluno in lista_alunos:
        print(f"Nome: {aluno['nome']} | Nota: {aluno['nota']}")

    time.sleep(10)
    os.system('cls' if os.name == 'nt' else 'clear')

def remover_aluno():
        if not lista_alunos:
            print("Nenhum aluno cadastrado.")
            time.sleep(3)
            return
        print("---- Alunos cadastrados na escola ----")
        for aluno in lista_alunos:
            print(f"Nome: {aluno['nome']}")
        aluno_remover = input("Qual será o aluno(a) removido(a)? ").strip()

        aluno_encontrado = None
        for aluno in lista_alunos:
            if aluno['nome'] == aluno_remover:
                aluno_encontrado = aluno
                break

        if aluno_encontrado:
            lista_alunos.remove(aluno_encontrado)
            print(f"Aluno {aluno_remover} removido com sucesso!")
        else:
            print(f"Aluno {aluno_remover} não encontrado!")
        time.sleep(3)

def salvar_dados():
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        for aluno in lista_alunos:
            arquivo.write(f"{aluno['nome']};{aluno['nota']}\n")

def carregar_dados():
    if os.path.exists("alunos.txt"):
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 2:
                    nome = dados[0]
                    nota = float(dados[1])
                    lista_alunos.append({"nome": nome, "nota": nota})

def calcular_media():
    if not lista_alunos:
        print("Nenhum Aluno(a) cadastrado(a)")
    else:
        soma_notas = sum(aluno['nota'] for aluno in lista_alunos)
        quantidade_alunos = len(lista_alunos)
        media = soma_notas / quantidade_alunos

        print(f"A média da turma é de {media:.2f}")
        time.sleep(3)

def buscar_aluno():
    nome_busca = input("Qual aluno você deseja ver? ")

    for aluno in lista_alunos:
        if aluno['nome'] == nome_busca:
            print(f"Nome: {aluno['nome']} | Nota: {aluno['nota']}")
            break

    else:
        print("Aluno não encontrado!")
    time.sleep(3)

carregar_dados()
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---- Menu principal ----")
    print("1. Cadastrar aluno(a)")
    print("2. Remover aluno(a)")
    print("3. Listar alunos(as)")
    print("4. Consultar aluno(a)")
    print("5. Calcular média da turma")
    print("6. Sair")
    escolha = input("Oque iremos fazer hoje?: ")

    if escolha == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        cadastro_aluno()

    elif escolha == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        remover_aluno()

    elif escolha == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        listar_alunos()

    elif escolha == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        buscar_aluno()

    elif escolha == "5":
        os.system('cls' if os.name == 'nt' else 'clear')
        calcular_media()

    elif escolha =="6":
        print("Saindo do sistema até logo...")
        salvar_dados()
        time.sleep(3)
        break
    else:
        print("Opção inválida, escolha 1, 2, 3, 4, 5 ou 6.")
        time.sleep(5)
