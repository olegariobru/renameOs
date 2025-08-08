import os
import pandas as pd

pasta = r'C:\Users\Suporte\Desktop\Renomear'  # ajuste seu caminho
csv_path = r'C:\Users\Suporte\Desktop\renomear.csv'  # caminho do arquivo Excel

# Ler Excel com pandas
df = pd.read_csv(csv_path, dtype={'nome_original': str})

# Criar dicionário do dataframe: {nome_original: sufixo}
renomear_map = dict(zip(df['nome_original'].astype(str), df['sufixo']))

os.chdir(pasta)

for arquivo in os.listdir():
    nome_sem_extensao, extensao = os.path.splitext(arquivo)
    if nome_sem_extensao in renomear_map:
        novo_nome = f"{nome_sem_extensao}_{renomear_map[nome_sem_extensao]}{extensao}"
        print(f"Renomeando: {arquivo} -> {novo_nome}")
        os.rename(arquivo, novo_nome)
    else:
        print(f"Pular arquivo: {arquivo} - não está na lista")

print("Renomeação concluída.")

