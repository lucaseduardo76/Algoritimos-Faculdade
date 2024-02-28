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
    
