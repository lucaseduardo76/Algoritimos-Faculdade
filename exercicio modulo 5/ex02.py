nadadores = [];
   
for i in range(7):
    nome_atual = input(f"Digite o nome do {i+1}° atleta: ");

    while True:
        tempo_atual = int(input("Digite o tempo em segundos desse nadador: "))

        if len(nadadores) > 0:
            verify = False
            for i in range(len(nadadores)):
                if(nadadores[i][1] == tempo_atual):  
                    verify = True

            if(verify == False):
                break;
            else:
                print("Tempo já inserido anteriormente")
        else:
            break;

    nadador_atual = [nome_atual, tempo_atual]
    nadadores.append(nadador_atual)    
        
ind_p = 0
ind_m = 0
t_m = 0

for i in range(7):
    ind_p = 0

    if i == 0:
        ind_m = i
    else:
        if nadadores[i][1] < ind_m:
            ind_m = i
        
    if ind_p < nadadores[i][1]:
        ind_p = i
        
    t_m += nadadores[i][1]

print(f"Nadador com melhor tempo: {nadadores[ind_m][0]} \n"
        f"Nadador com pior tempo: {nadadores[ind_p][0]} \n"
        f"Tempo médio dos nadadores: {t_m/7}")
