from json_utils import carregar_tarefas, salvar_tarefas

def opcoes():
    print('''
1. Adicionar tarefa
2. Listar tarefas
3. Marcar tarefa como concluída
4. Sair
''')
    
def menu():
    while True:
        opcoes()
        try:
            escolha = int(input('Escolha uma opção: '))
        except ValueError:
            print("Digite apenas números válidos.")
            continue

        if escolha == 1:
            titulo = input("Digite o título da tarefa: ")
            adicionar_tarefa(titulo)
        elif escolha == 2:
            listar_tarefas()
        elif escolha == 3:
            marcar_tarefa()
        elif escolha == 4:
            print("Encerrando programa")
            break

        else:
            print("Opção Inválida")

def adicionar_tarefa(titulo):
    tarefas = carregar_tarefas()
    nova_tarefa = {
        "titulo": titulo,
        "concluido": False
    }
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)

def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            status = "✅" if tarefa["concluido"] else "❌"
            print(f"{i}. {tarefa["titulo"]} - {status}")
            
def marcar_tarefa():
    tarefas = carregar_tarefas()
    listar_tarefas()
    try:
        numero = int(input("Qual número da tarefa que gostaria de marcar como concluida? "))
        indice = numero - 1
    except ValueError:
        print("Digite apenas números válidos.")
        return
    
    if numero < 1 or numero > len(tarefas):
        print("Número de tarefa inválido!")
        return

    tarefas[indice]["concluido"] = True
    salvar_tarefas(tarefas)
    print("Tarefa marcada como concluída com sucesso!")

menu()