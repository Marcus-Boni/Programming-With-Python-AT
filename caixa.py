from tabulate import tabulate
from utils import obter_data_formatada

def iniciar_atendimento(cliente_id):
    print(f"\nIniciando atendimento para Cliente {cliente_id} às {obter_data_formatada()}")
    return []

def adicionar_item(produtos, itens, produto_id, quantidade):
    for produto in produtos:
        if produto[0] == produto_id:
            if produto[2] >= quantidade:
                produto[2] -= quantidade
                itens.append([produto[0], produto[1], quantidade, produto[3], quantidade * produto[3]])
                print(f"Adicionado: {produto[1]} (Qtd: {quantidade})")
            else:
                print(f"Quantidade insuficiente para {produto[1]}. Disponível: {produto[2]}")
            break
    else:
        print("Produto não encontrado.")
    return itens

def finalizar_atendimento(cliente_id, itens):
    print(f"\nFinalizando atendimento para Cliente {cliente_id} às {obter_data_formatada()}")
    print(tabulate(itens, headers=["ID", "Produto", "Qtd", "Preço Unitário (R$)", "Total (R$)"], tablefmt="grid"))
    total = sum(item[4] for item in itens)
    print(f"Total: R${total:.2f}\n")
    return total

def exibir_resumo(clientes, total_vendas, produtos):
    print("\nResumo do Caixa:")
    print(tabulate(clientes, headers=["Cliente", "Total (R$)"], tablefmt="grid"))
    print(f"Total de vendas: R${total_vendas:.2f}")

    produtos_sem_estoque = [p for p in produtos if p[2] <= 0]
    if produtos_sem_estoque:
        print("\nProdutos sem estoque:")
        print(tabulate(produtos_sem_estoque, headers=["ID", "Produto", "Qtd", "Preço (R$)"], tablefmt="grid"))
    else:
        print("\nTodos os produtos possuem estoque disponível.")