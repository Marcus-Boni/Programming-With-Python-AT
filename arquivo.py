import csv

def ler_produtos(caminho_arquivo):
    produtos = []
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            next(leitor_csv) 
            for linha in leitor_csv:
                produtos.append([int(linha[0]), linha[1], int(linha[2]), float(linha[3])])
    except FileNotFoundError:
        print("Erro: Arquivo de produtos não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
    return produtos

def gravar_produtos(caminho_arquivo, produtos):
    try:
        with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
            escritor_csv = csv.writer(arquivo)
            escritor_csv.writerow(["ID", "Nome do Produto", "Quantidade em Estoque", "Preço (R$)"])
            for produto in produtos:
                escritor_csv.writerow(produto)
    except Exception as e:
        print(f"Erro ao gravar o arquivo: {e}")