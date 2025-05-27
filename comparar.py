import pandas as pd

# Carregar o Excel
df = pd.read_excel("mock_gicode.xlsx")

# Selecionar as colunas relevantes
df = df[['name', 'gicode jira', 'gicode feed']]

# Definir condições:
cond_iguais = (df['gicode jira'] == df['gicode feed']) & df['gicode jira'].notna()
cond_vazios = df['gicode jira'].isna() & df['gicode feed'].isna()
cond_diferentes = ~cond_iguais & ~cond_vazios  # inclui casos com apenas um valor

# Filtrar DataFrames
df_iguais = df[cond_iguais]
df_vazios = df[cond_vazios]
df_diferentes = df[cond_diferentes]

# Salvar arquivos .txt — campos vazios permanecem vazios
df_iguais.to_csv("iguais.txt", sep='\t', index=False, header=False)
df_vazios.to_csv("vazios.txt", sep='\t', index=False, header=False)
df_diferentes.to_csv("diferentes.txt", sep='\t', index=False, header=False)

print("Arquivos gerados com sucesso: iguais.txt, vazios.txt, diferentes.txt")
