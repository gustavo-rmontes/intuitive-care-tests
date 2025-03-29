import requests
from bs4 import BeautifulSoup

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