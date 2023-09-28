def ex01():
    palavra = input("Digite a palavra para tradução: ")
    length = len(palavra)

    if palavra[length-4:] == "dade":
        print(palavra[0: length-4] + "ty")
    else:
        print("Palavra não compativel")

def ex02():

    l1 = []
    l2 = []
    l_tot = []
    
    n_list = 1
    cont_l1 = 0
    cont_l2 = 0
    
    for i in range(2):
        term = 1

        while True:
            u = input(f"Digite o {term}° termo da {i+1}° lista: ")

            if n_list == 1:
                l1.append(u)
                cont_l1 += 1
            else:
                l2.append(u)
                cont_l2 += 1

            term += 1
            next = input("Você deseja inserir outro numero? [S/N]")
            if next != 's'and next != 'S':
                n_list = 2
                break
                
        
    if len(l1) == len(l2):
        for i in range(len(l1)):
            l_tot.append(l1[i] * l2[i])
    else:
        print("Tamanho das lista divergem!")

    print(f"A soma do produto dos vetores é: {sum(l_tot)}")

ex02()