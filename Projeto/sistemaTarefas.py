import json
import os
1
if not os.path.exists("gerenciadorTarefas.json"):
    object_json = json.dumps([], indent=2, ensure_ascii=False)

    with open("gerenciadorTarefas.json", "w", encoding='utf-8') as file:
        file.write(object_json)

def update(dicionario):

    object_json = json.dumps(dicionario, indent=2, ensure_ascii=False)

    with open("gerenciadorTarefas.json", "w", encoding='utf-8') as file:
        file.write(object_json)

#-----------------------------------------------------------------#

def read():
    with open("gerenciadorTarefas.json", encoding='utf-8') as file:
        dados = json.load(file)
    
    return dados
#-----------------------------------------------------------------#
def limpar_terminal():
    os.system('cls')





   

while True:
    dados = read()
    id = 1
    for i in range(len(dados)):        
        id = int(dados[i]['id']) + 1

    def listar():
        if len(dados): 
            print(f"Lista de tarefas: ")
            for u in range(len(dados)):
                print(f"{dados[u]['id']}° Tarefa: \n"
                    f"Responsável: {dados[u]['responsavel']} \n"
                    f"Descrição: {dados[u]['descricao']} \n"
                    f"Status: {dados[u]['status']} \n"
                    '------------------------------------------------ \n')
        else:
            print('Não há nenhuma tarefa! ') 
            
    
    acao = int(input(f"Bem vindo ao sistema de gerenciamento de tarefas: \n"
        f"Escolha uma das opções abaixo: \n"
        f"1° Adicionar Tarefas \n"
        f"2° Alterar Status \n"
        f"3° Editar Tarefa \n"
        f"4° Excluir Tarefa \n"
        f"5° Listar Tarefas \n"
        f"6° Encerrar Sistema \n"))
    
    if acao == 1:
        limpar_terminal()
        responsavel = input("Digite o nome do responsável pela tarefa: ")
        data = input("Digite a data limite para execução da tarefa: ")
        descricao = input("Digite a descricao da tarefa: ")

        dicionario = {
            "id": id,
            "responsavel": responsavel,
            "data": data,
            "descricao": descricao,
            "status": "Não iniciada"
        }
        dados.append(dicionario)
        update(dados)
        limpar_terminal()
    elif acao == 2:
        limpar_terminal()
        listar()
        if(len(dados)):
            tarefa = int(input("Digite o numero da tarefa que deseja alterar o status: "))
        
            for i in range(len(dados)):

                if(dados[i]['id'] == tarefa):
                    stat = int(input(f"1  - Em andamento \n"
                                f"2 - Finalizada \n"
                                f"Selecione o status que deseja aplicar \n"))
                    upData = ''
                    if(stat == 1):
                        upData = 'Em andamento'
                    elif(stat == 2):
                        upData = 'Finalizada'
                    
                    dados[i].update({'status': upData})
                    update(dados)
            limpar_terminal()     

    elif acao == 3:
        limpar_terminal()
        listar()
        if(len(dados)):
            tarefa = int(input("Digite o numero da tarefa que deseja editar: "))
            
            for i in range(len(dados)):

                if(dados[i]['id'] == tarefa):
                    edit = int(input(f"1  - Responsável \n"
                                f"2 - Data Limite \n"
                                f"3 - Descrição \n"
                                f"Selecione o dado que deseja editar: "))
                    
                    if(edit == 1):
                        resp = input("Digite o nome do novo responsável: ")
                        dados[i].update({'responsavel': resp})
                        update(dados)
                        limpar_terminal()
                    elif(edit == 2):
                        dat = input("Digite a nova data limite para a tarefa: ")
                        dados[i].update({'data': dat})
                        update(dados)
                        limpar_terminal()
                    elif(edit == 3):
                        desc = input("Digite a nova descrição para a tarefa: ")
                        dados[i].update({'descricao': desc})
                        update(dados)
                        limpar_terminal()
                    else:
                        limpar_terminal()
                        print('OPÇÃO INVÁLIDA')
            
    elif acao == 4:
        limpar_terminal()
        listar()
        if(len(dados)):
            verify = True
            while verify:
                tarefa = int(input("Digite o numero da tarefa que deseja excluir: "))
                if tarefa <= (len(dados)) and tarefa > 0:
                    verify = False

            c = input("Tem certeza que deseja excluir a tarefa? [S/N]: ")

            if(c == 's' or c == 'S'):
                
                dados.pop(tarefa - 1)

                for i in range(len(dados)):
                    dados[i].update({'id': i+1})
                update(dados)


            limpar_terminal()
        
              
    elif acao == 5:        
        limpar_terminal()
        listar()
    elif acao == 6:
        print('Obrigado!')
        break
        
        


