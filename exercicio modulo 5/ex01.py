termo_atual  = int(input("Digite o primeiro termo da P.A: "));
qnt_termos = int(input("Quantos termos essa P.A possui? "));
razao = int(input("Qual a razão da P.A: "));
pa = []; 
for i in range(qnt_termos):
    pa.append(termo_atual)
    termo_atual += razao       
print(f"Os termos da da P.A são {pa} \n"
    "A soma dos termos da P.A é {sum(pa)}")