def ex1():
    contato = {"@camilaqueiroz": "Camila Queiroz",
               "@paollaoliveirareal": "Paolla de oliveira"}
    
    contato.update({"@paollaoliveirareal": "Paolla"})
    print(len(contato))
    
    for i in contato.keys():
        print(i)

ex1()