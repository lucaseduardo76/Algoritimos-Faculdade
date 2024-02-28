relatorio = {}
while True:
    rz = input("Informe a razão social da empresa: [Para encerrar digite 0] ")
    print("")    
    if (rz == "0"):
          break
    vl = float(input("Informe o valor total de compra dessa empresa: "))    
    relatorio.update({rz: vl})
for k, v  in sorted(relatorio.items(), reverse=True):
     print(f"Cliente: {k} -> {v}")