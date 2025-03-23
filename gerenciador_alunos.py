def mostrar_menu():
    print("\nMenu:")
    print("1. Adicionar aluno e notas")
    print("2. Atualizar notas de um aluno")
    print("3. Remover aluno")
    print("4. Exibir alunos e notas")
    print("5. Calcular e exibir médias")
    print("6. Sair")

def adicionar_aluno(alunos):
    nome = input("Nome do aluno: ")
    notas = []
    for i in range(1, 5):
        nota = float(input(f"Nota {i}: "))
        notas.append(nota)
    alunos[nome] = notas
    print(f'Aluno "{nome}" adicionado com sucesso!')

def atualizar_notas(alunos):
    nome = input("Nome do aluno a atualizar: ")
    if nome in alunos:
        notas = []
        for i in range(1, 5):
            nota = float(input(f"Nova Nota {i}: "))
            notas.append(nota)
        alunos[nome] = notas
        print(f'Notas de "{nome}" atualizadas com sucesso!')
    else:
        print(f'Aluno "{nome}" não encontrado.')

def remover_aluno(alunos):
    nome = input("Nome do aluno a remover: ")
    if nome in alunos:
        del alunos[nome]
        print(f'Aluno "{nome}" removido com sucesso!')
    else:
        print(f'Aluno "{nome}" não encontrado.')

def exibir_alunos(alunos):
    if alunos:
        print("\nAlunos e suas notas:")
        for nome, notas in alunos.items():
            print(f'{nome}: {notas}')
    else:
        print("Nenhum aluno cadastrado.")

def calcular_medias(alunos):
    if alunos:
        print("\nMédias dos alunos:")
        for nome, notas in alunos.items():
            media = sum(notas) / len(notas)
            print(f'{nome}: {media:.2f}')
    else:
        print("Nenhum aluno cadastrado.")

def main():
    alunos = {
        "Ana": [8.5, 7.0, 9.2, 6.8],
        "Carlos": [5.5, 6.0, 7.5, 8.0],
        "Mariana": [9.0, 8.5, 10.0, 9.8],
        "Lucas": [6.5, 7.2, 5.8, 6.9],
        "Fernanda": [7.8, 8.2, 7.0, 8.5]
    }

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_aluno(alunos)
        elif escolha == '2':
            atualizar_notas(alunos)
        elif escolha == '3':
            remover_aluno(alunos)
        elif escolha == '4':
            exibir_alunos(alunos)
        elif escolha == '5':
            calcular_medias(alunos)
        elif escolha == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

    input("Pressione Enter para sair...")  # Mantém a janela aberta

if __name__ == "__main__":
    main()
