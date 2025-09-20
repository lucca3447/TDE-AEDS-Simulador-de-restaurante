cardapio = [
    {"nome": "Arroz branco", "preco": 5.00},
    {"nome": "Feijão carioca", "preco": 6.00},
    {"nome": "Farofa temperada", "preco": 4.00},
    {"nome": "Batata frita pequena", "preco": 8.00},
    {"nome": "Batata frita grande", "preco": 12.00},
    {"nome": "Salada verde", "preco": 7.00},
    {"nome": "Salada Caesar", "preco": 12.00},
    {"nome": "Frango grelhado", "preco": 15.00},
    {"nome": "Frango à milanesa", "preco": 18.00},
    {"nome": "Filé de peixe", "preco": 20.00},
    {"nome": "Filé de frango com molho", "preco": 19.00},
    {"nome": "Carne bovina acebolada", "preco": 22.00},
    {"nome": "Bife à parmegiana", "preco": 25.00},
    {"nome": "Strogonoff de frango", "preco": 23.00},
    {"nome": "Strogonoff de carne", "preco": 26.00},
    {"nome": "Lasanha de carne", "preco": 28.00},
    {"nome": "Lasanha de frango", "preco": 27.00},
    {"nome": "Espaguete ao sugo", "preco": 20.00},
    {"nome": "Espaguete à bolonhesa", "preco": 23.00},
    {"nome": "Ravioli de queijo", "preco": 24.00},
    {"nome": "Risoto de frango", "preco": 25.00},
    {"nome": "Risoto de camarão", "preco": 35.00},
    {"nome": "Camarão empanado", "preco": 30.00},
    {"nome": "Moqueca de peixe", "preco": 32.00},
    {"nome": "Moqueca de camarão", "preco": 38.00},
    {"nome": "Feijoada completa", "preco": 28.00},
    {"nome": "Costela bovina assada", "preco": 29.00},
    {"nome": "Picanha na chapa", "preco": 42.00},
    {"nome": "Churrasco misto", "preco": 39.00},
    {"nome": "Hambúrguer simples", "preco": 15.00},
    {"nome": "Hambúrguer duplo", "preco": 22.00},
    {"nome": "Cheeseburger", "preco": 18.00},
    {"nome": "X-Bacon", "preco": 23.00},
    {"nome": "Cachorro-quente", "preco": 12.00},
    {"nome": "Tábua de frios", "preco": 35.00},
    {"nome": "Porção de mandioca frita", "preco": 10.00},
    {"nome": "Porção de polenta frita", "preco": 11.00},
    {"nome": "Coxinha de frango", "preco": 6.00},
    {"nome": "Pastel de carne", "preco": 7.00},
    {"nome": "Pastel de queijo", "preco": 7.00},
    {"nome": "Empada de frango", "preco": 6.00},
    {"nome": "Torta salgada", "preco": 8.00},
    {"nome": "Sorvete de chocolate", "preco": 10.00},
    {"nome": "Sorvete de morango", "preco": 10.00},
    {"nome": "Pudim de leite", "preco": 8.00},
    {"nome": "Mousse de maracujá", "preco": 9.00},
    {"nome": "Torta de limão", "preco": 11.00},
    {"nome": "Bolo de chocolate", "preco": 9.00},
    {"nome": "Petit gateau", "preco": 15.00},
    {"nome": "Salada de frutas", "preco": 7.00},
    {"nome": "Água sem gás", "preco": 3.00},
    {"nome": "Água com gás", "preco": 4.00},
    {"nome": "Refrigerante lata", "preco": 6.00},
    {"nome": "Suco de laranja", "preco": 7.00},
    {"nome": "Suco de maracujá", "preco": 7.00},
    {"nome": "Suco de uva", "preco": 7.00},
    {"nome": "Suco de abacaxi", "preco": 7.00},
    {"nome": "Chá gelado", "preco": 6.00},
    {"nome": "Café expresso", "preco": 5.00},
    {"nome": "Cappuccino", "preco": 8.00},
    {"nome": "Chocolate quente", "preco": 9.00},
    {"nome": "Milkshake de chocolate", "preco": 12.00},
    {"nome": "Milkshake de morango", "preco": 12.00},
    {"nome": "Milkshake de baunilha", "preco": 12.00},
    {"nome": "Energético", "preco": 10.00},
    {"nome": "Suco detox", "preco": 9.00},
    {"nome": "Smoothie de frutas vermelhas", "preco": 14.00},
    {"nome": "Smoothie de banana", "preco": 12.00},
    {"nome": "Smoothie tropical", "preco": 13.00},
    {"nome": "Vitamina de mamão", "preco": 10.00},
    {"nome": "Vitamina de banana", "preco": 10.00},
    {"nome": "Vitamina de abacate", "preco": 11.00},
    
]

def exibir_cardapio():
    print("Cardápio: ")
    for i,prato in enumerate(cardapio):
        print(f"{i}:{prato["nome"]} - R$ {prato["preco"]:.2f} ")
    print("\n")

n_de_mesas = 10

pedidos_ativos =  [[] for i in range(n_de_mesas)]

def abrir_pedido(mesa):
    print("======ABRIR PEDIDO=====")
    exibir_cardapio()
    print("\n")
    
    id_prato = int(input("Qual o número do prato deseja pedir?\n"))
    quantidade = int(input("Qual a quantidade?"))
   
    pedidos_ativos[mesa].append((id_prato, quantidade))

    print(f"Pedido feito com sucesso!: {quantidade} x {cardapio[id_prato]['nome']}\n ")

def fechar_pedido(mesa):
    total= 0
    for prato_id, quantidade in pedidos_ativos[mesa]:
        total += cardapio[prato_id]["preco"]* quantidade

    print(f"Total da mesa {mesa+1}: {total:.2f} R$")

    pedidos_ativos[mesa] = []

def pedidos_ativos():
    print("=====PEDIDOS ATIVOS=====")
    for n_mesa, pedidos in enumerate(pedidos_ativos):
        if pedidos:
            print(f"Mesa {n_mesa+1}:")
            for prato_id, quantidade in pedidos:
                prato= cardapio[prato_id]
                print(f" {quantidade}x {prato['nome']} - R$ {prato['preco']:2.f} cada")
                print("\n")


