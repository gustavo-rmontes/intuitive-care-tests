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
