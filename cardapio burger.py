cardapio = ["Guarana","Coca cola","X burger","Cheddar n Onions","X bacon","X salada","Frango frito","Milk shake"]

def buscaCardapio(Ordem):
    pedidoEncontrado = False
    for i in cardapio:
        if Ordem.lower() in i.lower():
            pedidoEncontrado = True
    if pedidoEncontrado == True:
        print("Perfeito, iremos preparar seu" + Ordem + " Aguarde 10 minutos")
    else:
        print("Puxa, não encontramos seu pedido " + Ordem + " Tente outro pedido")
print("Bem vindo ao Busty Burgers, somos a melhor hamburguer da região, por favor, faça seu pedido")
print("Se deseja sair, digite /Exit")
saida = False
while saida == False:
    pedido = input("Qual seria o seu pedido?")
    if pedido == "/Exit":
        print("Muito obrigado por vir na Busty Burgers")
        saida = True
    else:
        buscaCardapio(pedido)
    
