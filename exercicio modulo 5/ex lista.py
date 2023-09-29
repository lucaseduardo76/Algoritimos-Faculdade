def ex1():

    termo_atual  = int(input("Digite o primeiro termo da P.A: "));
    qnt_termos = int(input("Quantos termos essa P.A possui? "));
    razao = int(input("Qual a razão da P.A: "));
    pa = []; 
    for i in range(qnt_termos):
        pa.append(termo_atual)
        termo_atual += razao       
    print(f"Os termos da da P.A são {pa} \n"
        "A soma dos termos da P.A é {sum(pa)}")
    
def ex2():
    nadadores = [];
   
    for i in range(7):
        nome_atual = input(f"Digite o nome do {i+1}° atleta: ");

        while True:
            tempo_atual = int(input("Digite o tempo em segundos desse nadador: "))

            if len(nadadores) > 0:
                verify = False
                for i in range(len(nadadores)):
                    if(nadadores[i][1] == tempo_atual):  
                        verify = True

                if(verify == False):
                    break;
                else:
                    print("Tempo já inserido anteriormente")
            else:
                break;

        nadador_atual = [nome_atual, tempo_atual]
        nadadores.append(nadador_atual)    
        
    ind_p = 0
    ind_m = 0
    t_m = 0

    for i in range(7):
        ind_p = 0

        if i == 0:
            ind_m = i
        else:
            if nadadores[i][1] < ind_m:
                ind_m = i
        
        if ind_p < nadadores[i][1]:
            ind_p = i
        
        t_m += nadadores[i][1]

    print(f"Nadador com melhor tempo: {nadadores[ind_m][0]} \n"
            f"Nadador com pior tempo: {nadadores[ind_p][0]} \n"
            f"Tempo médio dos nadadores: {t_m/7}")

def ex3():
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


def ex4():
    ver = True
    list_number = []
    middle_number = 0
    while ver == True:
        while True:
            number = int(input("Digite um numero inteiro positivo: [Para finalizar digite 0] \n"))

            if(number > 0):
                break
            elif (number == 0):
                if(len(list_number) % 2 != 0):
                    ver = False
                    break
                else:
                    print("Quantidade de itens invalida, adicione mais um numero para encerrar! \n")
            else:
                print("Valor inválido! \n")

        list_number.append(number)   
    middle_number = list_number[int((len(list_number)/2) - 0.5)]

   
    tot_sum = 1
    for i in range(middle_number, 0, -1):
        tot_sum *= i

    
    print(f"O fatorial de {middle_number} é {tot_sum}!")

ex4()
    
            
