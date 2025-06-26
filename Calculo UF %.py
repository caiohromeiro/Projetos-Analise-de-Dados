import pandas as pd
import openpyxl
import os

# Caminho do arquivo
caminho_arquivo = r'C:\Users\caio.silverio\OneDrive - Grupo Ultra\Documentos\Indicador Vendas Bases\List.  Enviada_Devol. Bruno COM.xlsx'

# Lendo o arquivo
df = pd.read_excel(caminho_arquivo)

# Somando os volumes
soma = df["Volume (m³)"].sum()

# Agrupando por UF e somando os volumes
soma_por_uf = df.groupby("UF Municipio")["Volume (m³)"].sum()

# Calculando o percentual de cada UF
percentual_por_uf = (soma_por_uf / soma) * 100

# Criando o DataFrame com os resultados e incluindo o nome do estado como coluna
resultado = pd.DataFrame({
    "UF Municipio": soma_por_uf.index,
    "Volume Total (m³)": soma_por_uf.values,
    "Percentual (%)": percentual_por_uf.values
})

# Salvando o arquivo na mesma pasta
diretorio = os.path.dirname(caminho_arquivo)
caminho_saida = os.path.join(diretorio, "Resumo_Por_UF.xlsx")
resultado.to_excel(caminho_saida, index=False, engine='openpyxl')

print(f"Arquivo salvo com sucesso em: {caminho_saida}")

