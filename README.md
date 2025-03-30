# Intuitive Care - estágio em SE

Este repositório reúne as soluções dos quatro testes técnicos do processo seletivo. Para facilitar a navegação, cada teste está organizado em uma pasta separada.

As implementações foram feitas da seguinte forma:
- Código em Python para os testes de programação;
- SQL compatível com PostgreSQL para os testes de banco de dados;
- Frontend do teste 4 desenvolvido em Vue.js.

## Estrutura do projeto

```shell
  ├── teste1
  │   └── anexos/
  │   └── scrap_html.py
  ├── teste2
  │   └── extract.py
  ├── teste3
  │   └── data/
  │   └── create_table.sql
  │   └── import_table.sql
  │   └── ultimo-ano.sql
  │   └── ultimo-3_meses.sql
  ├── teste4
  │   └── frontend/
  │   └── server/
  ├── .gitignore
  ├── requirements.txt
  └── Gustavo-Intuitive_care.postman_collection.json
```

## Tecnologias Utilizadas
- **Python** (para testes 1, 2 e backend do 4)
- **PostgreSQL** (para teste 3)
- **Vue.js** (frontend do teste 4)

## Instalação das Dependências
```bash
# Para os testes em Python
pip install -r requirements.txt

# Para o frontend do teste 4
cd teste4/frontend
npm install 
```

### Como rodar
**Teste 1**
```bash
cd teste1/
python scrap_html.py
```

**Teste 2**
```bash
cd teste2/
python extract.py
```

**Teste 4**
```bash
cd teste4/server/
python new_server.py
cd ../frontend/
npm run dev
```
