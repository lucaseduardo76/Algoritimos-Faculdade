#Crie uma função com o nome processar_dados que receba uma lista de dicionário e que faça as seguintes ações.

#[
#{‘nome’: ‘Lucas’, ‘idade’: 22, ‘salario’ 412},
#{‘nome’: ‘Mateus’, ‘idade’: 32, ‘salario’ 4212},
#{‘nome’: ‘Lula’, ‘idade’: 29, ‘salario’ 5412},
#{‘nome’: ‘Bolsonaro, ‘idade’: 52, ‘salario’ 4012}
#]

#- Imprima o nome da pessoa mais jovem
#- Imprima a média de idade das pessoas
#- imprima a soma total dos salário
#- Crie uma nova lista de dicionários com os mesmos dados da anterior, porém se a pessoa tiver mais de 30 anos aumente o salário dela em 10%

def processar_dados(dicionario):
    mediaIdade = 0
    salarioTotal = 0
    menorIdade = None
    novaLista = []
    somaIdade = 0

    for i in range(len(dicionario)):
        if menorIdade == None:
            menorIdade = dicionario[i]['idade']
        elif menorIdade > dicionario[i]['idade']:
            menorIdade = dicionario[i]['idade']
        
        somaIdade += dicionario[i]['idade']
        salarioTotal += dicionario[i]['salario']

        novoNome = dicionario[i]['nome']
        novaIdade = dicionario[i]['idade']

        if novaIdade > 30:
            novoSalario = dicionario[i]['salario'] + dicionario[i]['salario'] * 0.1
        else:
            novoSalario = dicionario[i]['salario']
        
        novoDicionario = {
            'nome': novoNome,
            'idade': novaIdade,
            'salario': novoSalario
        }
        novaLista.append(novoDicionario)
    
    mediaIdade = somaIdade/len(dicionario)

    print(f'A media de idade das pessoas é: {mediaIdade}')
    print(f'A soma de todos os salarios é: {salarioTotal}')
    print(f"O nome dicionario é: {novaLista}")

    for i in range(len(dicionario)):
        if menorIdade == dicionario[i]['idade']:
            print(f"A pessoa com menor idade é: {dicionario[i]['nome']}")

processar_dados([
{'nome': 'Lucas', 'idade': 22, 'salario': 412},
{'nome': 'Mateus', 'idade': 32, 'salario': 4212},
{'nome': 'Lula', 'idade': 19, 'salario': 5412},
{'nome': 'Bolsonaro', 'idade': 52, 'salario': 4012}
])
