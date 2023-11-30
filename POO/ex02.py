import json
import os
import random
import datetime

# Caso não exista o arquivo JSON de tarefas essa função irá criar
if not os.path.exists("data.json"):
    object_json = json.dumps([], indent=2, ensure_ascii=False)

    with open("data.json", "w", encoding='utf-8') as file:
        file.write(object_json)

#função que faz o update no JSON de tarefas
def updateData(dicionario):

    object_json = json.dumps(dicionario, indent=2, ensure_ascii=False)

    with open("data.json", "w", encoding='utf-8') as file:
        file.write(object_json)

#função que faz a leitura no JSON  de tarefas
def readData():
    with open("data.json", encoding='utf-8') as file:
        dados = json.load(file)
    
    return dados

data = readData()

for i in range(len(data["todasAsRodadas"])):
    for u in range(len(data["todasAsRodadas"][i]["perguntas"])):
       data["todasAsRodadas"][i]["perguntas"][u]["respostas"]  = random.shuffle(data["todasAsRodadas"][i]["perguntas"][u]["respostas"])
       updateData(data)



