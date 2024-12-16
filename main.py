from arquivo import ler_produtos, gravar_produtos
from caixa import iniciar_atendimento, adicionar_item, finalizar_atendimento, exibir_resumo
from utils import obter_data_formatada

def main():
    caminho_arquivo = "produtos.csv"
    produtos = ler_produtos(caminho_arquivo)

    if not produtos:
        print("Erro: Nenhum produto carregado. Verifique o arquivo.")
        return

    clientes = []
    total_vendas = 0
    cliente_id = 1

    print(f"Caixa aberto às {obter_data_formatada()}")

    while True:
        print("\n1. Iniciar atendimento")
        print("2. Fechar caixa")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            itens = iniciar_atendimento(cliente_id)
            while True:
                produto_id = int(input("Digite o ID do produto (0 para finalizar): "))
                if produto_id == 0:
                    break
                quantidade = int(input("Digite a quantidade: "))
                itens = adicionar_item(produtos, itens, produto_id, quantidade)
            
            total_cliente = finalizar_atendimento(cliente_id, itens)
            clientes.append([f"Cliente {cliente_id}", total_cliente])
            total_vendas += total_cliente
            cliente_id += 1

        elif opcao == "2":
            exibir_resumo(clientes, total_vendas, produtos)
            gravar_produtos(caminho_arquivo, produtos)
            print(f"\nCaixa fechado às {obter_data_formatada()}")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()