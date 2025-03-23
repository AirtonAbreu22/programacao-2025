class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome, quantidade):
        if nome in self.produtos:
            self.produtos[nome] += quantidade
        else:
            self.produtos[nome] = quantidade
        print(f'Produto "{nome}" adicionado com quantidade {quantidade}.')

    def remover_produto(self, nome):
        if nome in self.produtos:
            del self.produtos[nome]
            print(f'Produto "{nome}" removido do estoque.')
        else:
            print(f'Produto "{nome}" não encontrado.')

    def atualizar_quantidade(self, nome, quantidade):
        if nome in self.produtos:
            self.produtos[nome] = quantidade
            print(f'Quantidade do produto "{nome}" atualizada para {quantidade}.')
        else:
            print(f'Produto "{nome}" não encontrado.')

    def exibir_produtos(self):
        if self.produtos:
            print("Produtos no estoque:")
            for nome, quantidade in self.produtos.items():
                print(f'- {nome}: {quantidade}')
        else:
            print("O estoque está vazio.")

def main():
    estoque = Estoque()
    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Atualizar quantidade")
        print("4. Exibir produtos")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            estoque.adicionar_produto(nome, quantidade)
        elif escolha == '2':
            nome = input("Nome do produto a remover: ")
            estoque.remover_produto(nome)
        elif escolha == '3':
            nome = input("Nome do produto a atualizar: ")
            quantidade = int(input("Nova quantidade: "))
            estoque.atualizar_quantidade(nome, quantidade)
        elif escolha == '4':
            estoque.exibir_produtos()
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
