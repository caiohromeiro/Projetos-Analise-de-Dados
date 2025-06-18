import pandas as pd
import requests

# ========================
# Parte 1: Baixar o arquivo do SharePoint (simulado)
# ========================
# Substitua esta URL pelo link direto de download do SharePoint
url_sharepoint = "https://exemplo.com/arquivo.xlsx"

# Nome do arquivo local
arquivo_local = "dados_sharepoint.xlsx"

# Simulação do download
response = requests.get(url_sharepoint)
with open(arquivo_local, 'wb') as f:
    f.write(response.content)

# ========================
# Parte 2: Ler o Excel
# ========================
df = pd.read_excel(arquivo_local)
print(df.head())

# ========================
# Parte 3: Atualizar dataset no Power BI
# ========================
TENANT_ID = 'seu-tenant-id'
CLIENT_ID = 'seu-client-id'
CLIENT_SECRET = 'seu-client-secret'
WORKSPACE_ID = 'seu-workspace-id'
DATASET_ID = 'seu-dataset-id'

def get_access_token():
    url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': 'https://analysis.windows.net/powerbi/api/.default'
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get('access_token')

def refresh_dataset(token):
    url = f"https://api.powerbi.com/v1.0/myorg/groups/{WORKSPACE_ID}/datasets/{DATASET_ID}/refreshes"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 202:
        print("Atualização iniciada com sucesso.")
    else:
        print("Erro ao iniciar atualização:", response.text)

# Executar atualização
token = get_access_token()
refresh_dataset(token)
