import json

# Lê o arquivo JSON
with open('faturamento.json', 'r') as file:
    dados = json.load(file)

faturamento_diario = dados["faturamento_diario"]

# Calcula a média, o menor e o maior valor
dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
menor_faturamento = min(dias_com_faturamento)
maior_faturamento = max(dias_com_faturamento)
dias_acima_media = len([valor for valor in dias_com_faturamento if valor > media_mensal])

print("Menor valor de faturamento:", menor_faturamento)
print("Maior valor de faturamento:", maior_faturamento)
print("Número de dias com faturamento acima da média mensal:", dias_acima_media)
