import pandas as pd

df = pd.read_excel("C:/Users/PC/Desktop/softexPython/notas_alunos.xlsx")

df["Média"] = (df["Nota 1"] + df["Nota 2"]) / 2

df.loc[(df['Faltas'] > 5) | (df['Média'] < 7), 'Situação'] = 'Reprovado'
df.loc[(df['Faltas'] < 5) & (df['Média'] >= 7), 'Situação'] = 'Aprovado'
print(df)

df.to_csv('C:/Users/PC/Desktop/softexPython/alunos_situacao.csv')

print()

max_f = df["Faltas"].max()
print(f"O maior número de faltas foi: {max_f} faltas.")

print()

mediag = df["Média"].sum() / 4
print(f"A média geral das notas dos alunos: {mediag}.")

print()

max_f = df["Média"].max()
print(f"A maior média entre os alunos foi de: {max_f}.")
