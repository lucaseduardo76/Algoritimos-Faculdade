dados = []

numero_conta = input("Digite o numero da conta para ver o saldo: ")
for i in range(len(dados)):
    if(dados[i]['numero_da_conta'] == numero_conta):
        print(f"Nome: {dados[i]['nome']} \n"
            f"Saldo: {dados[i]['saldo']}")