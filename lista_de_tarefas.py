#Este projeto vai ser um aplicativo de linha de comando para voce gerenciar suas tarefas. Voce podera adicionar novas tarefas, ve-las, marcar como concluidas e ate remover tarefas. É um passo fundamental para entender como criar aplicativos interativos que persistem dados (mesmo que de forma simples, neste cado).
#Oque voce vai aprender:
#Manipulação de Listas, funções, laços de repetição, condicionais, entrada e saida de dados.

#Funcionalidades: #Adicionar tarefa, visualizar tarefas, marcar tarefa como concluida, remover tarefa, menu interativo, tratamento de erros.

tarefas = []
def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")
def visualizar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")
def marcar_tarefa_concluida(indice):
    try:
        tarefa = tarefas.pop(indice - 1)
        print(f"Tarefa '{tarefa}' marcada como concluída!")
    except IndexError:
        print("Índice inválido. Tente novamente.")
def remover_tarefa(indice):
    try:
        tarefa = tarefas.pop(indice - 1)
        print(f"Tarefa '{tarefa}' removida com sucesso!")
    except IndexError:
        print("Índice inválido. Tente novamente.")
def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Visualizar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            tarefa = input("Digite a tarefa: ")
            adicionar_tarefa(tarefa)
        elif escolha == '2':
            visualizar_tarefas()
        elif escolha == '3':
            indice = int(input("Digite o índice da tarefa a ser marcada como concluída: "))
            marcar_tarefa_concluida(indice)
        elif escolha == '4':
            indice = int(input("Digite o índice da tarefa a ser removida: "))
            remover_tarefa(indice)
        elif escolha == '5':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    menu()
#Este é um exemplo simples de um aplicativo de lista de tarefas em Python.
#Ele permite que o usuário adicione, visualize, marque como concluídas e remova tarefas de uma lista.
#Você pode expandir este projeto adicionando funcionalidades como salvar as tarefas em um arquivo, carregar tarefas de um arquivo, ou até mesmo implementar uma interface gráfica.
#Essas adições podem ser feitas conforme você for se familiarizando mais com Python e suas bibliotecas.
#Lembre-se de testar cada funcionalidade e tratar possíveis erros, como entradas inválidas.
#Divirta-se programando e gerenciando suas tarefas!