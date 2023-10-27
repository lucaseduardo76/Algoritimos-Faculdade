import json
import os
import datetime

if not os.path.exists("gerenciadorTarefas.json"):
    object_json = json.dumps([], indent=2, ensure_ascii=False)

    with open("gerenciadorTarefas.json", "w", encoding='utf-8') as file:
        file.write(object_json)

if not os.path.exists("gerenciadorUsuarios.json"):
    object_json = json.dumps([], indent=2, ensure_ascii=False)

    with open("gerenciadorUsuarios.json", "w", encoding='utf-8') as file:
        file.write(object_json)


def updateTarefas(dicionario):

    object_json = json.dumps(dicionario, indent=2, ensure_ascii=False)

    with open("gerenciadorTarefas.json", "w", encoding='utf-8') as file:
        file.write(object_json)


def readTarefas():
    with open("gerenciadorTarefas.json", encoding='utf-8') as file:
        dados = json.load(file)
    
    return dados


def updateUsuarios(dicionario):

    object_json = json.dumps(dicionario, indent=2, ensure_ascii=False)

    with open("gerenciadorUsuarios.json", "w", encoding='utf-8') as file:
        file.write(object_json)


def readUsuarios():
    with open("gerenciadorUsuarios.json", encoding='utf-8') as file:
        dados = json.load(file)
    
    return dados


def limpar_terminal():
    os.system('cls')


def validarData(data_string):
    try:
        data = datetime.datetime.strptime(data_string, '%d/%m/%Y').date()
        return data
    except ValueError:
        return None
    
    
def formatarData(data):
    return data.strftime('%d/%m/%Y')


    

def listarTarefas():
    if len(dadosTarefa): 
        print(f"Lista de tarefas: ")
        for u in range(len(dadosTarefa)):
            print(f"{dadosTarefa[u]['id']}° Tarefa: \n"
                f"Responsável: {dadosTarefa[u]['responsavel']} \n"
                f"Descrição: {dadosTarefa[u]['descricao']} \n"
                f"Status: {dadosTarefa[u]['status']} \n"
                '------------------------------------------------ \n')
    else:
        print('Não há nenhuma tarefa! ') 

def listarUsuarios():
    if len(dadosUsuario): 
        print(f"Lista de usuarios: ")
        for u in range(len(dadosUsuario)):
            print(f"Id: {dadosUsuario[u]['id']} \n"
                f"Nome: {dadosUsuario[u]['nome']} \n"
                '------------------------------------------------ \n')
    else:
        print('Não há nenhum usuario cadastrado! ') 

while True:
    dadosTarefa = readTarefas()
    dadosUsuario = readUsuarios()

    acaoGeral = int(input(f"Bem vindo ao sistema de gerenciamento de tarefas: \n"
        f"Escolha uma das opções abaixo: \n"
        f"1° Gerenciar Usuarios \n"
        f"2° Gerenciar Tarefas \n"
        f"3° Encerrar Sistema \n"))
    
    if acaoGeral == 1:
        acaoUsuario = 0
        while acaoUsuario != 4:
            limpar_terminal()
            idUsuario = 1
            for i in range(len(dadosUsuario)):
                idUsuario = int(dadosUsuario[i]['id']) + 1

            acaoUsuario = int(input(f"Escolha uma das opções abaixo: \n"
                f"1° Cadastrar novo usuario \n"
                f"2° Editar usuario \n"
                f"3° Excluir usuario \n"
                f"4° Voltar ao menu principal\n"))
            
            if acaoUsuario == 1:
                limpar_terminal()
                nome = input("Digite o nome do novo funcionario: ")

                dicionario = {
                    "id": idUsuario,
                    "nome": nome
                }
                dadosUsuario.append(dicionario)
                updateUsuarios(dadosUsuario)
                limpar_terminal()

            elif acaoUsuario == 2:
                limpar_terminal()
                listarUsuarios()
                if(len(dadosUsuario)):
                    usuario = int(input("Digite o Id usuario que deseja editar: "))
                    
                    for i in range(len(dadosUsuario)):
                        if(dadosUsuario[i]['id'] == usuario):                            
                            user = input("Digite o nome do novo responsável: ")
                            dadosUsuario[i].update({'nome': user})
                            updateUsuarios(dadosUsuario)
                            limpar_terminal()                           

            elif acaoUsuario == 3:
                limpar_terminal()
                listarUsuarios()
                if(len(dadosUsuario)):
                    
                    usuario = int(input("Digite o Id do usuario que deseja excluir: "))
                    
                    
                    idInvalido = False
                    for u in range(len(dadosUsuario)):
                        indice = u - 1
                        if(dadosUsuario[indice]['id'] == usuario):
                            limpar_terminal()
                            print(f"----------------------------------------- \n"
                                  f"Id: {dadosUsuario[indice]['id']} \n"
                                  f"Nome: {dadosUsuario[indice]['nome']} \n"
                                  f"-----------------------------------------")
                            c = input("Tem certeza que deseja excluir o usuario? [S/N]: ")
                        
                            if(c == 's' or c == 'S'):
                                dadosUsuario.pop(indice)
                                updateUsuarios(dadosUsuario)
                            else:
                                idInvalido = True

                    limpar_terminal()
                    if idInvalido:
                        print('Id não existe!')
            elif acaoUsuario == 4:
                limpar_terminal()
    
    elif acaoGeral == 2:
        if len(dadosUsuario) > 0:
            limpar_terminal()

            idTarefa = 1
            for i in range(len(dadosTarefa)):        
                idTarefa = int(dadosTarefa[i]['id']) + 1

            acaoTarefa = int(input(f"Escolha uma das opções abaixo: \n"
                f"1° Adicionar Tarefas \n"
                f"2° Alterar Status \n"
                f"3° Editar Tarefa \n"
                f"4° Excluir Tarefa \n"
                f"5° Listar Tarefas \n"
                f"6° Encerrar Sistema \n"))
            
            if acaoTarefa == 1:
                limpar_terminal()
                veirfyId = True
                while veirfyId:                
                    listarUsuarios()
                    idResp = int(input("Digite o Id do responsável pela tarefa: "))
                    for i in range(len(dadosUsuario)):
                        if dadosUsuario[i]['id'] == idResp:
                            veirfyId = False
                        if veirfyId:
                            print("Id inexistente!")
                
                
                #PARAMOS AQUI  NA VERIFICAÇÃO SE O FUNCIONARIO JÁ TEM ALGUMA TAREFA NESSA DATA
                verifyData = True
                while verifyData:
                    data = input("Digite a data limite para execução da tarefa: (DD/MM/YYYY): ")
                    if validarData(data):
                        data = formatarData(validarData(data))
                        verifyData = False                 

                descricao = input("Digite a descricao da tarefa: ")

                dicionario = {
                    "id": idTarefa,
                    "idColaborador": idResp,
                    "data": data,
                    "descricao": descricao,
                }
                dadosTarefa.append(dicionario)
                updateTarefas(dadosTarefa)
                limpar_terminal()

            elif acaoTarefa == 2:
                limpar_terminal()
                listarTarefas()
                if(len(dadosTarefa)):
                    tarefa = int(input("Digite o numero da tarefa que deseja alterar o status: "))
                
                    for i in range(len(dadosTarefa)):

                        if(dadosTarefa[i]['id'] == tarefa):
                            stat = int(input(f"1  - Em andamento \n"
                                        f"2 - Finalizada \n"
                                        f"Selecione o status que deseja aplicar \n"))
                            upData = ''
                            if(stat == 1):
                                upData = 'Em andamento'
                            elif(stat == 2):
                                upData = 'Finalizada'
                            
                            dadosTarefa[i].update({'status': upData})
                            updateTarefas(dadosTarefa)
                    limpar_terminal()     

            elif acaoTarefa == 3:
                limpar_terminal()
                listarTarefas()
                if(len(dadosTarefa)):
                    tarefa = int(input("Digite o numero da tarefa que deseja editar: "))
                    
                    for i in range(len(dadosTarefa)):

                        if(dadosTarefa[i]['id'] == tarefa):
                            edit = int(input(f"1  - Responsável \n"
                                        f"2 - Data Limite \n"
                                        f"3 - Descrição \n"
                                        f"Selecione o dado que deseja editar: "))
                            
                            if(edit == 1):
                                resp = input("Digite o nome do novo responsável: ")
                                dadosTarefa[i].update({'responsavel': resp})
                                updateTarefas(dadosTarefa)
                                limpar_terminal()
                            elif(edit == 2):
                                dat = input("Digite a nova data limite para a tarefa: ")
                                dadosTarefa[i].update({'data': dat})
                                updateTarefas(dadosTarefa)
                                limpar_terminal()
                            elif(edit == 3):
                                desc = input("Digite a nova descrição para a tarefa: ")
                                dadosTarefa[i].update({'descricao': desc})
                                updateTarefas(dadosTarefa)
                                limpar_terminal()
                            else:
                                limpar_terminal()
                                print('OPÇÃO INVÁLIDA')
                    
            elif acaoTarefa == 4:
                limpar_terminal()
                listarTarefas()
                if(len(dadosTarefa)):
                    verify = True
                    while verify:
                        tarefa = int(input("Digite o numero da tarefa que deseja excluir: "))
                        if tarefa <= (len(dadosTarefa)) and tarefa > 0:
                            verify = False

                    c = input("Tem certeza que deseja excluir a tarefa? [S/N]: ")

                    if(c == 's' or c == 'S'):
                        
                        dadosTarefa.pop(tarefa - 1)

                        for i in range(len(dadosTarefa)):
                            dadosTarefa[i].update({'id': i+1})
                        updateTarefas(dadosTarefa)


                    limpar_terminal()
                
                    
            elif acaoTarefa == 5:        
                limpar_terminal()
                listarTarefas()
            elif acaoTarefa == 6:
                print('Obrigado!')
                break
        else:
           print('É necessário cadastrar um usuario para criar uma tarefa!')  
            


