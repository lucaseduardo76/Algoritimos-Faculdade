def escreve():
    import json

    dicionario=[{
        'nome': "Lucas Eduardo",
        "idade": "22 pra 23",
        "cidade": "Eunápolis" 
    },{
        'nome': "blabla Eduardo",
        "idade": "22 pra 23",
        "cidade": "Eunápolis" 
    },{
        'nome': "carlos Eduardo",
        "idade": "22 pra 23",
        "cidade": "Eunápolis" 
    }

    ]

    object_json = json.dumps(dicionario, indent=2)

    with open("test.json", "w") as file:
        file.write(object_json)

#-----------------------------------------------------------------#

##def ler():
#    import json

 #   with open("test.json", encoding='utf-8') as file:
  #      dados = json.load(file)


   # print(f"Meu nome é {dados['nome']} tenho {dados['idade']} anos e estou esperando em Deus uma vaga como programador!")


escreve()  