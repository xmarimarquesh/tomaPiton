agenda = {"gabriel":["123132","234234"]}
tell=[]

def incluirNovoNome():
    print("\n","=-"*30,"\n")
    nome = input("Digite o nome do contato: ")
    qtd_tel = int(input("Quantos números de telefone deseja adicionar a este contato?\n "))
    for i in range(qtd_tel):
        telefone = input("Digite o telefone de seu contato: ")
        tell.append(telefone)

    agenda[nome] = tell
    print("Contato adicionado com sucesso!")

def incluirTelefone():
    try:
        print("\n","=-"*30,"\n")
        nome = input("Digite o nome do contato: ")
    
        if nome not in agenda:
            if input("Ops! Este contato não consta em sua agenda, deseja adiciona-lo? \n1-Sim\n2-Não\n") == "1":
                incluirNovoNome()
                raise NameError
            else:
                raise NameError
        
        qtd_tel = int(input('Quantos telefones deseja adicionar? '))
        for i in range(qtd_tel):
            telefone = input("Digite o telefone de seu contato: ")
            tell.append(telefone)

        agenda[nome] = tell
        print("Número adicionado com sucesso!")
    except NameError:
        print()

def excluirTelefone():
    print("\n","=-"*30,"\n")
    nome = input("Digite o nome do contato: ")
    print(agenda[nome])
    num = input("Digite o número em que deseja excluir: ")

    for i in agenda[nome]:
        if i == num:
            i.pop()
    print(agenda)
    print("Número excluído com sucesso!")

def excluirContato():
    print("\n","=-"*30,"\n")
    nome = input("Digite o nome do contato: ")
    agenda[nome].pop()

    print(agenda)
    print("Contato excluído com sucesso!")

def consultarTelefone():
    print("\n","=-"*30,"\n")
    nome = input("Digite o nome do contato: ")

    print(f"Números de {nome}: {agenda[nome]}")

while True:
    print("\n","=-"*30,"\n")
    print(f"Sua agenda: {agenda}")

    op = input("O que deseja fazer? \n1-Adicionar novo contato\n2-Incluir telefone a um contato extistente\n3-Excluir um telefone\n4-Excluir um contato\n5-Consultar contato\n6-Sair\n:")

    match op:
        case "1":
            while True:
                incluirNovoNome()
                adc = input("Deseja adicionar mais um contato?\n1-Sim\n2-Não\n ")
                if adc == '2':
                    break
        case "2":
            incluirTelefone()
        case "3":
            excluirTelefone()
        case "4":
            excluirContato()
        case "5":
            consultarTelefone()
        case "6":
            print("Sua agenda: ",agenda)
            break


    