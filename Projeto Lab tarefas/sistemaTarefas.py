import json
import os

def escreve(dicionario):

    object_json = json.dumps(dicionario, indent=2, ensure_ascii=False)

    with open("gerenciadorTarefas.json", "w", encoding='utf-8') as file:
        file.write(object_json)

#-----------------------------------------------------------------#

def ler():
    with open("gerenciadorTarefas.json", encoding='utf-8') as file:
        dados = json.load(file)
    
    return dados

def limpar_terminal():
    os.system('cls')



dados = ler()

while True:
    acao = int(input(f"Bem vindo ao sistema de gerenciamento de tarefas: \n"
        f"Escolha uma das opções abaixo: \n"
        f"1° Adicionar Tarefas \n"
        f"2° Editar tarefa \n"
        f"3° Excluir tarefa \n"
        f"4° Listar tarefas \n"
        f"5° Encerrar sistema"))
    
    if acao == 1:
        responsavel = input("Digite o nome do responsável pela tarefa: ")
        data = input("Digite a data limite para execução da tarefa: ")
        descricao = input("Digite a descricao da tarefa: ")

        dicionario = {
            "responsavel": responsavel,
            "data": data,
            "descricao": descricao,
            "status": "Não iniciada"
        }
        dados.append(dicionario)
        escreve(dados)

