import requests
from bs4 import BeautifulSoup
import os, shutil

gov_url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

response = requests.get(url=gov_url) 
print("[url] Response status: " + str(response.status_code))

soup = BeautifulSoup(response.text, 'html.parser')

links_anexos = []
texto_anexos = ['Anexo I.', 'Anexo II.']

# Gera a lista de links com .pdf e que tem Anexo no texto de <a>
for a in soup.find_all('a', href=True):
    texto_link = a.text 
    href_link = a['href'] 
    if texto_link in texto_anexos and href_link.endswith('.pdf'):
        links_anexos.append(a['href'])

# Cria a pasta 'anexos' se ela não existir
os.makedirs("anexos", exist_ok=True)

# Baixa os PDFs
for link in links_anexos:
    file_name = os.path.basename(link)
    file_path = os.path.join("anexos", file_name)
    print(f"Baixando {file_name}...")
    
    try:
        pdf_response = requests.get(link, stream=True)
        pdf_response.raise_for_status() 
        
        with open(file_path, 'wb') as f:
            f.write(pdf_response.content)
        print(f"{file_name} salvo!\n")
    
    except Exception as e:
        print(f"Erro ao baixar {file_name}: {e}\n")

shutil.make_archive('anexos-compact', 'zip', 'anexos')
