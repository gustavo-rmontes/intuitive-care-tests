import pandas as pd
import pdfplumber
import shutil

dataset_path = '../teste1/anexos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'

# Lista para armazenar os dados das tabelas
tables = []

with pdfplumber.open(dataset_path) as pdf:
    for i in range(2, len(pdf.pages)): 
        page = pdf.pages[i]
        table = page.extract_table()

        if table:
            df = pd.DataFrame(table[1:], columns=table[0])  
            tables.append(df)

# Concatenar tabelas como dataframe
final_df = pd.concat(tables, ignore_index=True)

# print(final_df.head())

print(final_df.columns)
final_df.columns = final_df.columns.str.strip()

mapping = {"OD": "Seg. Odontológica", "AMB": "Seg. Ambulatorial"}

final_df["OD"] = final_df["OD"].map(lambda x: mapping.get(x, x))
final_df["AMB"] = final_df["AMB"].map(lambda x: mapping.get(x, x))


# Salvar em .csv
final_df.to_csv('tabela.csv', index=False)

# Compactar tabela.csv para tabela.zip
shutil.make_archive("Teste_Gustavo", "zip", ".", "tabela.csv")