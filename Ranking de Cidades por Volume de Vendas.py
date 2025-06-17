import pandas as pd
df= pd.read_excel(r'C:\Users\caio.silverio\OneDrive - Grupo Ultra\Arquivos de Chat do Microsoft Teams\Cidades_200km_Raio_Estudo_Vera.xlsx')
print(df.head(5))
total = df['Volume'].sum()
print(f'Total da Colune; {total}')
media= df['Volume'].mean()
print(f'Média da coluna: {media}')
top5 = df.nlargest(5, 'Volume')
print(top5)
df['Porcentagem'] = (df['Volume'] / total) * 100

import matplotlib.pyplot as plt

# Criar gráfico de barras com os volumes por cidade

top10 = df.nlargest(10, 'Volume')

plt.figure(figsize=(12, 6))
plt.bar(df['cidade'], df['Volume'], color='skyblue')
plt.xlabel('cidade')
plt.ylabel('Volume')
plt.title('Volume por Cidade')
plt.xticks(rotation=45, ha='right') # Rotaciona os nomes das cidades para melhor leitura
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
print(df.head())
pd.set_option('display.max_rows', None)
print(df)
