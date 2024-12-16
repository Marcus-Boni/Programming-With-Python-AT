# Sistema de Caixa de Supermercado

## Descrição do Projeto

Este projeto é um sistema de caixa para um supermercado, implementado em Python. Ele permite:

- Gerenciar produtos e seus estoques.
- Processar compras de múltiplos clientes sequencialmente.
- Registrar vendas e gerar relatórios.
- Atualizar o arquivo de produtos automaticamente após cada sessão de operação do caixa.

## Funcionalidades

1. **Abertura do Caixa:**

   - Leitura do arquivo `produtos.csv` contendo as informações dos produtos disponíveis no estoque.
   - Validação dos dados carregados para evitar inconsistências.

2. **Atendimento de Clientes:**

   - Identifica cada cliente sequencialmente (exemplo: Cliente 1, Cliente 2, etc.).
   - Permite ao atendente inserir itens comprados com:
     - ID do produto.
     - Quantidade desejada.
   - Calcula automaticamente o valor total de cada item com base na quantidade e no preço unitário.
   - Atualiza o estoque do produto após cada compra.
   - Gera uma "Nota Fiscal" com os detalhes do atendimento, incluindo:
     - ID e nome do produto.
     - Quantidade comprada.
     - Preço unitário.
     - Preço total por item.
     - Valor total da compra.

3. **Fechamento do Caixa:**

   - Exibe um resumo das vendas realizadas:
     - Lista de clientes atendidos com seus totais de compra.
     - Total geral arrecadado no período.
   - Lista produtos sem estoque.
   - Atualiza o arquivo `produtos.csv` com os dados mais recentes do estoque.

## Estrutura do Projeto

```plaintext
├── main.py           # Arquivo principal para execução do programa.
├── caixa.py          # Contém as funções relacionadas à operação do caixa.
├── produtos.csv      # Arquivo com os produtos do supermercado.
└── utils.py          # Funções auxiliares em geral.
└── arquivo.py        # Função auxiliar para leitura e gravação de arquivos.
```

### Exemplo do Arquivo `produtos.csv`

```csv
ID,Nome do Produto,Quantidade em Estoque,Preço (R$)
1,Arroz,50,5.49
2,Feijão,30,7.99
3,Açúcar,20,3.29
4,Sal,10,2.50
5,Macarrão,40,4.75
```

## Requisitos

- **Linguagem:** Python 3.8+
- **Bibliotecas Utilizadas:**
  - `csv` para manipulação do arquivo de produtos.
  - `tabulate` para exibição formatada de tabelas no terminal. (Instale com `pip install tabulate`)

## Como Executar

1. Certifique-se de que você tem o Python instalado em seu computador.
2. Instale a biblioteca `tabulate` executando:
   ```bash
   pip install tabulate
   ```
3. Organize os arquivos do projeto na estrutura descrita acima.
4. Execute o programa principal:
   ```bash
   python main.py
   ```

## Fluxo do Programa

1. O programa inicia carregando o arquivo `produtos.csv` e exibindo os produtos disponíveis.
2. O atendente pode realizar o atendimento de vários clientes, inserindo os produtos comprados e gerando notas fiscais individuais.
3. Ao fechar o caixa, o sistema exibe:
   - Resumo das vendas realizadas.
   - Produtos que ficaram sem estoque.
   - Total geral arrecadado.
4. O arquivo `produtos.csv` é atualizado automaticamente com os novos dados de estoque.

## Exemplos de Saída

### Nota Fiscal (Exemplo)

```plaintext
Cliente 1 - Nota Fiscal
+----+----------------+------------+--------------+--------------+
| ID | Nome do Produto | Quantidade | Preço Unitário | Preço Total |
+----+----------------+------------+--------------+--------------+
|  1 | Arroz          |          2 |          5.49 |        10.98 |
|  3 | Açúcar         |          1 |          3.29 |         3.29 |
+----+----------------+------------+--------------+--------------+
TOTAL: R$ 14.27
```

### Resumo Final

```plaintext
Resumo do Caixa:
+-----------+----------------+
| Cliente   | Total (R$)     |
+-----------+----------------+
| Cliente 1 |          14.27 |
| Cliente 2 |          23.47 |
+-----------+----------------+
TOTAL GERAL: R$ 37.74

Produtos sem estoque:
+----+----------------+----------+------------+
| ID | Nome do Produto | Estoque  | Preço (R$) |
+----+----------------+----------+------------+
|  4 | Sal            |        0 |       2.50 |
+----+----------------+----------+------------+
```

## Marcus Boni 🤙

Desenvolvido como parte de um exercício para aprendizado de boas práticas em Python, com foco em manipulação de arquivos, lógica de programação e geração de relatórios.

---

