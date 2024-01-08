import random
import time

# Listas de valores para simular dados aleatórios

nomes = ["João", "Maria", "Pedro", "Ana", "Carlos"]
cargos = ["Gerente", "Analista", "Assistente", "Desenvolvedor"]
senioridades = ["Júnior", "Pleno", "Sênior"]
tempos_de_casa = [1, 2, 3, 4, 5]
ids_usados = []

# Gerando registros aleatórios de funcionários
def gera_registro_funcionario():
    funcionario_id = random.randint(1,100000)
    while funcionario_id in ids_usados:
        funcionario_id = random.randint(1,100000)

    ids_usados.append(funcionario_id)
    nome = random.choice(nomes)
    cargo = random.choice(cargos)
    salario = round(random.uniform(2500.0, 16000.0), 2)
    tempo_de_casa = random.choice(tempos_de_casa)
    senioridade = random.choice(senioridades)
    
    return {
        "ID": funcionario_id,
        "Nome": nome,
        "Cargo": cargo,
        "Salário": salario,
        "Tempo de Casa": tempo_de_casa,
        "Senioridade": senioridade
    }



def calcular_total_salarios(registros):
    time_inicio = time.time()
    total_salarios = sum(registro["Salário"] for registro in registros)
    time_final = time.time()
    timeresultado = time_final - time_inicio
    print(timeresultado)
    return total_salarios


def remover_registros(registros, num_registros_para_remover):
    if num_registros_para_remover > len(registros):
        return "Número de registros a serem removidos é maior que o total de registros."
    
    novos_registros = registros[:-num_registros_para_remover]
    return novos_registros






# Gerar 5 registros de funcionários aleatórios
registros = [gera_registro_funcionario() for _ in range(40000)]

# Mostrar os registros gerados
for registro in registros:
    print(registro)
    
# Usando a função para calcular o total dos salários dos registros gerados anteriormente
total_salarios = calcular_total_salarios(registros)
print(f"O total dos salários é: R$ {total_salarios:.2f}")

# Supondo que 'registros' seja a lista dos seus registros existentes
# Remover 12 mil registros
registros = remover_registros(registros, 12000)

# Verificar o número atual de registros
print(f"Agora restam {len(registros)} registros.")
total_salarios = calcular_total_salarios(registros)
print(f"O total dos salários é: R$ {total_salarios:.2f}")
