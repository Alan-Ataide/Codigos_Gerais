import pandas as pd

import csv


# Ler o arquivo Excel
df = pd.read_excel(r'c:\user\seu_arquivo.xlsx')

# Converter o DataFrame para CSV separando cada palavra por ponto e vírgula e adicionando aspas
df.to_csv(r'c:\user\seu_arquivo.csv', index=False, sep=';', quoting=csv.QUOTE_NONE, quotechar='', escapechar='\\')

# Ler o arquivo CSV gerado
with open(r'c:\user\seu_arquivo.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Modificar cada linha para adicionar aspas apenas no início e no final
modified_lines = ['"' + line.strip().rstrip(';') + '"' for line in lines]

# Escrever o novo arquivo CSV com aspas apenas no início e no final de cada linha
with open(r'c:\user\seu_arquivo_final.csv', 'w', encoding='utf-8', newline='') as file:
    file.write('\n'.join(modified_lines))
