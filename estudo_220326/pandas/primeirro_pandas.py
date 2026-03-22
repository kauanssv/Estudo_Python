import pandas as pd

df = pd.read_excel(r"C:\Users\Pichau\Documents\Estudo_Python\Arquivos\Saúde Mental na Adolescência.xlsx")
df["Qual a sua idade ?"] = df["Qual a sua idade ?"].str.extract(r"(\d+)")
df["Qual a sua idade ?"] = df["Qual a sua idade ?"].astype(float)
filtro = df[df["Qual a sua idade ?"] > 15]
print(filtro)