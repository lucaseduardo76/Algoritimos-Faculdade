import json
import os
import datetime

# Caso não exista o arquivo JSON de tarefas essa função irá criar
if not os.path.exists("gerenciadorTarefas.json"):
    object_json = json.dumps([], indent=2, ensure_ascii=False)

    with open("gerenciadorTarefas.json", "w", encoding='utf-8') as file:
        file.write(object_json)


# Caso não exista o arquivo JSON de usuarios essa função irá criar
if not os.path.exists("gerenciadorUsuarios.json"):
    object_json = json.dumps([], indent=2, ensure_ascii=False)

    with open("gerenciadorUsuarios.json", "w", encoding='utf-8') as file:
        file.write(object_json)

#função que faz o update no JSON de tarefas
def updateTarefas(dicionario):

    object_json = json.dumps(dicionario, indent=2, ensure_ascii=False)

    with open("gerenciadorTarefas.json", "w", encoding='utf-8') as file:
        file.write(object_json)

#função que faz a leitura no JSON  de tarefas
def readTarefas():
    with open("gerenciadorTarefas.json", encoding='utf-8') as file:
        dados = json.load(file)
    
    return dados

#função que faz o updates do JSON de usuarios
def updateUsuarios(dicionario):

    object_json = json.dumps(dicionario, indent=2, ensure_ascii=False)

    with open("gerenciadorUsuarios.json", "w", encoding='utf-8') as file:
        file.write(object_json)


#função que faz a leitura do JSON de usuarios
def readUsuarios():
    with open("gerenciadorUsuarios.json", encoding='utf-8') as file:
        dados = json.load(file)
    
    return dados

#função que faz limpeza do terminal
def limpar_terminal():
    os.system('cls')

#função que faz a validação das datas inseridas
def validarData(data_string):
    try:
        data = datetime.datetime.strptime(data_string, '%d/%m/%Y').date()
        return data
    except ValueError:
        return None
    
#função que formata data no padrão (DD/MM/YYYY) 
def formatarData(data):
    return data.strftime('%d/%m/%Y')


    
#função que faz a listagem das tarefas
def listarTarefas():
    if len(dadosTarefa): 
        print(f"Lista de tarefas: \n")
        for u in range(len(dadosTarefa)):
            for i in range(len(dadosUsuario)):
                if dadosTarefa[u]['idColaborador'] == dadosUsuario[i]['id']:
                    print(f"Id da Tarefa: {dadosTarefa[u]['id']}\n"
                    f"Titulo da Tarefa: {dadosTarefa[u]['tituloTarefa']} \n"      
                    f"Nome do Responsável: {dadosUsuario[i]['nome']} \n"
                    f"Data: {dadosTarefa[u]['data']} \n"
                    f"Descrição: {dadosTarefa[u]['descricao']} \n"                
                    '------------------------------------------------ \n')
    else:
        print('Não há nenhuma tarefa! ') 

#função que faz a listagem dos usuarios
def listarUsuarios():
    if len(dadosUsuario): 
        print(f"Lista de usuarios: ")
        for u in range(len(dadosUsuario)):
            print(f"Id: {dadosUsuario[u]['id']} \n"
                f"Nome: {dadosUsuario[u]['nome']} \n"
                '------------------------------------------------ \n')
    else:
        print('Não há nenhum usuario cadastrado! ') 

#função que mostra todas as datas das tarefas do usuario escolhida
def dataIndisponivel(idColabora):
    dadosTarefa = readTarefas()
    print(f'Essas são as datas em que esse colaborador NÃO está disponivel \n'
          f"------------------------------------------------------------------ \n")
    for i in range(len(dadosTarefa)):
        if(dadosTarefa[i]['idColaborador'] == idColabora):
            print(f"Titulo da tarefa: {dadosTarefa[i]['tituloTarefa']} \n"
                  f"Data da tarefa: {dadosTarefa[i]['data']}\n"
          f"------------------------------------------------------------------ \n")

limpar_terminal()
#Iniciando o sistema com um while  True
while True:
    dadosTarefa = readTarefas() #Armazenando os dados do JSON das tarefas na variavel
    dadosUsuario = readUsuarios() #Armazenando os dados do JSON dos usuarios na variavel

    #Menu principal do sistema
    acaoGeral = int(input(f"Bem vindo ao sistema de gerenciamento de tarefas: \n"
        f"Escolha uma das opções abaixo: \n"
        f"1° Gerenciar Usuarios \n"
        f"2° Gerenciar Tarefas \n"
        f"3° Encerrar Sistema \n"))
    
    limpar_terminal()
    if acaoGeral == 1: #ação de entrar no gerenciamento de sistema
        acaoUsuario = 0
        while acaoUsuario != 5: #Se a acaousuario for o numero 4 esse looping é encerrado e o sistema volta ao menu principal

            idUsuario = 1
            #looping que verifica qual o proximo ID que deve ser destinado à um novo usuario (colaborador)
            for i in range(len(dadosUsuario)):
                idUsuario = int(dadosUsuario[i]['id']) + 1

            #Menu do gerenciamento de usuarios
            acaoUsuario = int(input(f"Escolha uma das opções abaixo: \n"
                f"1° Cadastrar novo usuario \n"
                f"2° Editar usuario \n"
                f"3° Excluir usuario \n"
                f"4° Listar usuarios \n"
                f"5° Voltar ao menu principal\n"))
            
            if acaoUsuario == 1: #entrando no cadastro de usuarios
                limpar_terminal()
                nome = input("Digite o nome do novo funcionario: ")

                dicionario = {
                    "id": idUsuario,
                    "nome": nome
                }
                dadosUsuario.append(dicionario)
                updateUsuarios(dadosUsuario)
                limpar_terminal()

            elif acaoUsuario == 2:#entrando na opção de edição de usuarios
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

            elif acaoUsuario == 3: #entrando na opção de excluir usuario
                limpar_terminal()
                listarUsuarios()
                if(len(dadosUsuario)): #verificando se ja existe usuario cadastrado
                    
                    Idusuario = int(input("Digite o Id do usuario que deseja excluir: ")) #pegando id do usuario que deve ser excluido
                    idInvalido = True
                    for u in range(len(dadosUsuario)):#Iniciando looping  para  encontrar o ID que foi digitado pelo usuario
                        indice = u - 1
                        if(dadosUsuario[indice]['id'] == Idusuario):#Conferindo se o usuario atual do looping é o usuario que deve ser deletado
                            limpar_terminal()
                            #Mostrando para o usuario qual o id e o nome do usuario que será deletado
                            print(f"----------------------------------------- \n"
                                  f"Id: {dadosUsuario[indice]['id']} \n"
                                  f"Nome: {dadosUsuario[indice]['nome']} \n"
                                  f"-----------------------------------------")
                            c = input("Tem certeza que deseja excluir o usuario? [S/N]: ") #pedindo uma confirmação para a exclusão
                        
                            if(c == 's' or c == 'S'):
                                for i in range(len(dadosTarefa)):
                                    indTarefas = i - 1
                                    if dadosTarefa[indTarefas]['idColaborador'] == dadosUsuario[indice]['id']:                                        
                                        dadosTarefa.pop(indTarefas)
                                        updateTarefas(dadosTarefa)

                                dadosUsuario.pop(indice)
                                updateUsuarios(dadosUsuario)
                        else:
                            idInvalido = False

                    limpar_terminal()
                    if idInvalido:
                        print('Id não existe!')
            elif acaoUsuario == 4:
                limpar_terminal()
                listarUsuarios()
            elif acaoUsuario == 5:
                limpar_terminal()
    
    elif acaoGeral == 2: #entrando na ação de tarefas
        if len(dadosUsuario) > 0: #Verificando se existe algum usuario cadastrado, para só assim poder entrar no menu de tarefas
            acaoTarefa = 0
            while acaoTarefa != 5: #iniciando looping que permeia as ações da tarefa              

                idTarefa = 1
                for i in range(len(dadosTarefa)): #looping for que indica qual será o proximo ID a ser adicionado na proxima tarefa cadastrada        
                    idTarefa = int(dadosTarefa[i]['id']) + 1

                #menu de tarefas
                acaoTarefa = int(input(f"Escolha uma das opções abaixo: \n"
                    f"1° Adicionar Tarefas \n"
                    f"2° Editar Tarefa \n"
                    f"3° Excluir Tarefa \n"
                    f"4° Listar Tarefas \n"
                    f"5° Voltar ao menu principal \n"))
                
                if acaoTarefa == 1: #Entrando na adição de tarefas
                    limpar_terminal()

                    titulo = input("Digite o titulo da tarefa: ")
                    
                    veirfyId = True
                    while veirfyId: #looping que verifica se o usuario (colaborador) escolhido para a tarefa existe           
                        listarUsuarios()
                        idResp = int(input("Digite o Id do responsável pela tarefa: "))
                        for i in range(len(dadosUsuario)):
                            if dadosUsuario[i]['id'] == idResp:
                                veirfyId = False
                        if veirfyId:
                            limpar_terminal()
                            print("Id inexistente!")
                    
                    
                    
                    verifyData = True
                    while verifyData: #Looping que verifica se a data inserida é uma data valida e se o usuario esta disponivel
                        data = input("Digite a data para execução da tarefa (DD/MM/YYYY): ")
                        if validarData(data):
                            data = formatarData(validarData(data))
                                
                            # Verifica se o funcionário já tem uma tarefa na mesma data
                            funcionario_disponivel = True
                            for i in range(len(dadosTarefa)):
                                if dadosTarefa[i]['idColaborador'] == idResp and dadosTarefa[i]['data'] == data:
                                    funcionario_disponivel = False
                                    limpar_terminal()
                                    print('FUNCIONÁRIO INDISPONÍVEL PARA ESTA DATA!')
                                    dataIndisponivel(idResp)
                                    break 

                            if funcionario_disponivel:
                                verifyData = False  # Sai do loop se o funcionário estiver disponível
                            else:
                                print('Por favor, escolha uma data diferente.')
                        else:
                            limpar_terminal()
                            print("Data inválida!")
            

                    descricao = input("Digite a descricao da tarefa: ")
                    
                    #adicionando todas as informações recolhidas em um dicionario de tarefas
                    dicionario = {
                        "id": idTarefa,
                        'tituloTarefa': titulo,
                        "idColaborador": idResp,
                        "data": data,
                        "descricao": descricao,
                    }
                    dadosTarefa.append(dicionario)
                    updateTarefas(dadosTarefa)
                    limpar_terminal()

                elif acaoTarefa == 2: #Entrando na edição de tarefas
                    limpar_terminal()
                    listarTarefas()
                    if(len(dadosTarefa)): #verificando se existem tarefas criadas, se não existir não há tarefas para editar!
                        tarefa = int(input("Digite o numero de Id da tarefa que deseja editar: ")) #pedindo ID da tarefa
                        
                        for i in range(len(dadosTarefa)):
                            
                            if(dadosTarefa[i]['id'] == tarefa):#se encontrar a tarefa, exibe o menu de edição

                                edit = int(input(f"1  - Titulo da tarefa \n"
                                            f"2 - Responsável \n"
                                            f"3 - Descrição \n"
                                            f"Selecione o dado que deseja editar: "))
                                
                                if(edit == 1):#entra na condicional para trocar o titulo da tarefa
                                    limpar_terminal()
                                    titulo = input("Digite o novo titulo para está tarefa: ")
                                    dadosTarefa[i].update({'tituloTarefa': titulo})
                                    updateTarefas(dadosTarefa)
                                    limpar_terminal()
                                elif(edit == 2):#entra na condicional para trocar o id do novo responsavel pela tarefa

                                    verifyId = True                                    
                                    while verifyId:
                                        disponivel = True
                                        limpar_terminal()              
                                        listarUsuarios()
                                        idResp = int(input("Digite o id do novo responsável por essa tarefa: "))
                                        for u in range(len(dadosUsuario)):
                                            if dadosUsuario[u]['id'] == idResp:                                                                                           
                                                for o in range(len(dadosTarefa)):
                                                    #Verifica se o novo responsavel tem disponibilidade nessa data para assumir essa tarefa
                                                    if(dadosTarefa[o]['idColaborador'] == idResp and dadosTarefa[o]['data'] == dadosTarefa[i]['data']):                                                        
                                                        disponivel = False

                                        #Se tiver disponibilidade faz um update no idColaborador
                                        if disponivel:
                                            verifyId = False
                                            dadosTarefa[i].update({'idColaborador': idResp})
                                            
                                        
                                    
                                    updateTarefas(dadosTarefa)
                                    limpar_terminal()
                                elif(edit == 3):#entra na condicional para alterar a nova descrição para a tarefa

                                    limpar_terminal()
                                    desc = input("Digite a nova descrição para a tarefa: ")
                                    dadosTarefa[i].update({'descricao': desc})
                                    updateTarefas(dadosTarefa)
                                    limpar_terminal()
                                else:
                                    limpar_terminal()
                                    print('OPÇÃO INVÁLIDA')
                        
                elif acaoTarefa == 3: #Entra na condicional para excluir a tarefa

                    limpar_terminal()
                    listarTarefas()
                    if(len(dadosTarefa)): #verifica se existe alguma tarefa, pois se não existir não tem como excluir nada

                        idTarefa = int(input("Digite o Id da tarefa que deseja excluir: "))
                        for i in range(len(dadosTarefa)):
                            
                            if len(dadosTarefa) - 1 >= i: #verificação que não deixa o looping dar erro após apagar uma tarefa
                                if dadosTarefa[i]['id'] == idTarefa:
                                    for u in range(len(dadosUsuario)):
                                        if len(dadosTarefa) - 1 >= i: #verificação que não deixa o looping dar erro após apagar uma tarefa
                                            if dadosUsuario[u]['id'] == dadosTarefa[i]['idColaborador']:
                                                limpar_terminal()
                                                print(f"-----------------------------------------------------\n"
                                                f"Titulo da Tarefa: {dadosTarefa[i]['tituloTarefa']} \n"
                                                f"Colaborador da Tarefa: {dadosUsuario[u]['nome']} \n"
                                                f"-----------------------------------------------------\n")

                                                c = input("Tem certeza que deseja excluir a tarefa? [S/N]: ")
                                                if c == 'S' or c == 's':
                                                    dadosTarefa.pop(i)
                                                    updateTarefas(dadosTarefa)
                        limpar_terminal()
                    else:
                        limpar_terminal()
                        print("Não existem tarefas cadastradas!")
                        
                elif acaoTarefa == 4: #condicional que entra na listagem de tarefas
                    limpar_terminal()
                    listarTarefas()
                elif acaoTarefa == 5: #condicional que volta para o menu principal
                    limpar_terminal()
            
        else:
           limpar_terminal()
           print('É necessário cadastrar pelo menos um usuario para criar uma tarefa!')  
            
    elif acaoGeral == 3:
        limpar_terminal()
        print("Obrigado por usar meu sistema, att Lucas Eduardo!")
        break

