def ex1():
    contato = {"@camilaqueiroz": "Camila Queiroz",
               "@paollaoliveirareal": "Paolla de oliveira",
               "@Adrianaoliveira": "Adriana oliveira"}
    
    contato.update({"@paollaoliveirareal": "Paolla"})
    print(len(contato))
    
    for i in contato.keys():
        print(i)
    
    for i in contato.values():
        print(i)

    for key, valor in sorted(contato.items()):
        print(f"{key} -> {valor}")


def ex2():
    from operator import itemgetter

    contato = {"@camilaqueiroz": "1.76",
               "@paollaoliveirareal": "1.68",
               "@Adrianaoliveira": "1.86"}
    
    
    copia = contato

    print(copia)    


