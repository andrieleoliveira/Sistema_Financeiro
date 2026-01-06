pessoas = []
vendas = []
contas_receber = []
contas_pagar = []

# Função para adicionar uma pessoa nova
def cadastrar_pessoa():
    print("\n--- Cadastro de Pessoa ---")
    # Pegando os dados do usuário
    nome = input("Nome: ").strip()
    cpf = input("CPF: ").strip()
    telefone = input("Telefone: ").strip()

    # cadastrando a pessoa
    pessoa = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone
    }

    pessoas.append(pessoa)
    print(f"Pessoa '{nome}' cadastrada!")

# Função para mostrar todo mundo que tá cadastrado
def listar_pessoas():
    print("\n--- Pessoas Cadastradas ---")
    
    # Se a lista tá vazia, não tem o que mostrar
    if len(pessoas) == 0:
        print("Nenhuma pessoa cadastrada ainda.")
        return 

    for i in range(len(pessoas)):
        p = pessoas[i] # Pega a pessoa da lista pelo índice
        print(f"{i} - {p['nome']} | CPF: {p['cpf']} | Tel: {p['telefone']}")

# Função para registrar uma venda - a venda consequentemente vai gerar uma conta a receber
def lancar_venda():
    print("\n--- Lançar Venda ---")
    
    if len(pessoas) == 0:
        print("Não há pessoas cadastradas! Cadastre uma pessoa primeiro.")
        return

    # Mostra a lista pra pessoa escolher
    listar_pessoas()
    
    indice_str = input("Escolha o índice da pessoa: ")
    indice = int(indice_str)

    # Vê se o índice existe na lista
    if indice < 0 or indice >= len(pessoas):
        print("Esse índice não existe!")
        return 
    
    pessoa = pessoas[indice]

    descricao = input("Descrição da venda: ").strip()
    
    valor_str = input("Valor da venda: R$ ").replace(",", ".")
    valor = float(valor_str) 
    
    # Cria a "ficha" da venda
    venda = {
        "pessoa": pessoa,
        "descricao": descricao,
        "valor": valor
    }
    
    vendas.append(venda)

    contas_receber.append({
        "pessoa": pessoa,
        "valor": valor,
        "descricao": descricao
    })

    print("Venda lançada! E já tá lá em Contas a Receber!")

def listar_contas_receber():
    print("\n--- Contas a Receber ---")
    if len(contas_receber) == 0:
        print("Nenhuma conta a receber. Uhul?")
        return
        
    for i in range(len(contas_receber)):
        conta = contas_receber[i]
        pessoa = conta["pessoa"]
        valor = conta["valor"]
        descricao = conta["descricao"]
        print(f"{i} - {pessoa['nome']} | R$ {valor:.2f} | {descricao}")

# Função pra cadastrar as despesas do usuario
def cadastrar_conta_pagar():
    print("\n--- Cadastro de Conta a Pagar ---")
    descricao = input("Descrição da despesa: ").strip()
    categoria_despesa = input("Categoria da despesa (luz, aluguel, etc): ").strip()
    
    valor_str = input("Valor da despesa: R$ ").replace(",", ".")
    valor = float(valor_str) 

    # Cria a "ficha" da conta
    conta = {
        "descricao": descricao,
        "categoria": categoria_despesa,
        "valor": valor
    }

    contas_pagar.append(conta)
    print("Conta a pagar cadastrada!")

def listar_contas_pagar():
    print("\n--- Contas a Pagar ---")
    if len(contas_pagar) == 0:
        print("Nenhuma conta a pagar cadastrada. Que bom!")
        return
        
    for i in range(len(contas_pagar)):
        c = contas_pagar[i]
        print(f"{i} - {c['descricao']} | Categoria: {c['categoria']} | R$ {c['valor']:.2f}")

# Funcao Fluxo de Caixa 
def visualizar_fluxo_caixa():
    print("\n===== FLUXO DE CAIXA =====")
    
    # Zera o total antes de começar a somar
    total_receber = 0
    # Passa por cada item na lista de contas_receber
    for c in contas_receber:
        # Pega o valor da conta atual e soma no total
        total_receber = total_receber + c["valor"]

    # Mesma coisa pras contas a pagar
    total_pagar = 0
    for c in contas_pagar:
        total_pagar = total_pagar + c["valor"]

    # Saldo é o que entra menos o que sai
    saldo = total_receber - total_pagar

    print(f"Total a Receber: R$ {total_receber:.2f}")
    print(f"Total a Pagar:   R$ {total_pagar:.2f}")
    print("----------------------------")
    print(f"Saldo Final:     R$ {saldo:.2f}")

# Menu de opçoes para o usuário
def menu():
    # Loop infinito -  Só para quando o usuário digita "0"
    while True:
        print("\n===== SISTEMA FINANCEIRO =====")
        print("1 - Cadastrar Pessoa")
        print("2 - Lançar Venda")
        print("3 - Listar Pessoas")
        print("4 - Listar Contas a Receber")
        print("5 - Cadastrar Contas a Pagar")
        print("6 - Listar Contas a Pagar")
        print("7 - Visualizar Fluxo de Caixa")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_pessoa()
        elif opcao == "2":
            lancar_venda()
        elif opcao == "3":
            listar_pessoas()
        elif opcao == "4":
            listar_contas_receber()
        elif opcao == "5":
            cadastrar_conta_pagar()
        elif opcao == "6":
            listar_contas_pagar()
        elif opcao == "7":
            visualizar_fluxo_caixa()
        elif opcao == "0":
            print("Saindo...")
            break 
        else:
            print("Opa! Opção inválida! Tenta de novo.")
menu()