import requests

gov_url = 'https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos'

response = requests.get(url=gov_url) 
print("[url] Response status: " + str(response.status_code))

