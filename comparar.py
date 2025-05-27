import pandas as pd

# Carregar o Excel
df = pd.read_excel("mock_gicode_comparacao.xlsx")

# Comparação
df['iguais'] = df['gicode jira'] == df['gicode feed']
df['ambos vazios'] = df[['gicode jira', 'gicode feed']].isnull().all(axis=1)
df['um vazio'] = df[['gicode jira', 'gicode feed']].isnull().any(axis=1) & ~df['ambos vazios']

# Conjuntos únicos
jira_set = set(df['gicode jira'].dropna())
feed_set = set(df['gicode feed'].dropna())

so_jira = jira_set - feed_set
so_feed = feed_set - jira_set
iguais = jira_set & feed_set

# Salvar resultados em arquivos .txt
with open("valores_iguais.txt", "w") as f:
    f.write("\n".join(sorted(iguais)))

with open("so_no_jira.txt", "w") as f:
    f.write("\n".join(sorted(so_jira)))

with open("so_no_feed.txt", "w") as f:
    f.write("\n".join(sorted(so_feed)))

df[df['iguais'] == True].to_string("linhas_iguais.txt", index=False)
df[df['iguais'] == False].to_string("linhas_diferentes.txt", index=False)
df[df['um vazio'] == True].to_string("linhas_vazias.txt", index=False)

print("Arquivos .txt criados com sucesso!")

