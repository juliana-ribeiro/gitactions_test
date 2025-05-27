import pandas as pd

# Carregar o Excel
df = pd.read_excel("mock_gicode.xlsx")

# Selecionar as colunas relevantes
df = df[['name', 'gicode jira', 'gicode feed']]

# Identificar condições específicas
cond_iguais = (df['gicode jira'] == df['gicode feed']) & df['gicode jira'].notna()
cond_vazios = df['gicode jira'].isna() & df['gicode feed'].isna()
cond_diferentes = ~cond_iguais & ~cond_vazios  # inclui qualquer um nulo ou diferentes

# Filtrar DataFrames
df_iguais = df[cond_iguais]
df_vazios = df[cond_vazios]
df_diferentes = df[cond_diferentes]

# Salvar em arquivos .txt (somente valores, sem cabeçalhos)
df_iguais.to_csv("iguais.txt", sep='\t', index=False, header=False)
df_vazios.to_csv("vazios.txt", sep='\t', index=False, header=False)
df_diferentes.to_csv("diferentes.txt", sep='\t', index=False, header=False)

print("Arquivos 'iguais.txt', 'vazios.txt' e 'diferentes.txt' criados com sucesso.")

