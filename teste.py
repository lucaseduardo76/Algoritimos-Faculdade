import datetime

def validar_data(data_string):
    try:
        data = datetime.datetime.strptime(data_string, '%d/%m/%Y').date()
        return data
    except ValueError:
        return None
    
def formatar_data(data):
    return data.strftime('%d/%m/%Y')

# Solicita ao usuário que insira uma data
data_digitada = input("Digite uma data no formato YYYY-MM-DD: ")

data_valida = validar_data(data_digitada)

if data_valida:
    print(f"A data {formatar_data(data_valida)} é válida.")
else:
    print("A data digitada não é válida. Certifique-se de usar o formato YYYY-MM-DD.")