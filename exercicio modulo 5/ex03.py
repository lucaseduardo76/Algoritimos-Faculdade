import random 
nomes = []
cont = 1
while True:

    nome = input(f"Digite o nome do {cont}° comprador da rifa: [Para finalizar digite 0] ")

    if(nome == '0'):
        break
    else: 
        nomes.append(nome)
        cont += 1
    
print(f"O ganhador do premio foi {random.choice(nomes)}")