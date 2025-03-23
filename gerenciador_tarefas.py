def mostrar_menu():
    print("\nMenu:")
    print("1. Adicionar nova tarefa")
    print("2. Marcar tarefa como concluída")
    print("3. Listar todas as tarefas")
    print("4. Sair")

def adicionar_tarefa(tarefas):
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição da tarefa: ")
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "status": "Pendente"
    }
    tarefas.append(tarefa)
    print(f'Tarefa "{titulo}" adicionada com sucesso!')

def marcar_concluida(tarefas):
    titulo = input("Título da tarefa a marcar como concluída: ")
    for tarefa in tarefas:
        if tarefa["titulo"] == titulo:
            tarefa["status"] = "Concluído"
            print(f'Tarefa "{titulo}" marcada como concluída!')
            return
    print(f'Tarefa "{titulo}" não encontrada.')

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nTarefas Pendentes:")
    for tarefa in tarefas:
        if tarefa["status"] == "Pendente":
            print(f'Título: {tarefa["titulo"]}, Descrição: {tarefa["descricao"]}')

    print("\nTarefas Concluídas:")
    for tarefa in tarefas:
        if tarefa["status"] == "Concluído":
            print(f'Título: {tarefa["titulo"]}, Descrição: {tarefa["descricao"]}')

def main():
    tarefas = []

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_tarefa(tarefas)
        elif escolha == '2':
            marcar_concluida(tarefas)
        elif escolha == '3':
            listar_tarefas(tarefas)
        elif escolha == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

    input("Pressione Enter para sair...")  # Mantém a janela aberta

if __name__ == "__main__":
    main()
