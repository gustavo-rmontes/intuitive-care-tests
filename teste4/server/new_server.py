import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={
    r"/search": {
        "origins": ["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:8080"],
        "methods": ["GET", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

data_path = "Relatorio_cadop.csv"
df = pd.read_csv(data_path, sep=";", encoding="utf-8")

# Endpoint de busca
@app.get("/search")
def search_data():
    """
    Filtra o dataframe com base nos parâmetros:
    - column: nome da coluna para filtrar (opcional)
    - query: texto para busca (opcional)
    - limit: número máximo de resultados (opcional)
    """
    try:
        # Obter parâmetros da URL
        column_name = request.args.get('column', default=None)
        search_query = request.args.get('query', default=None)
        limit = int(request.args.get('limit', default=10))
        
        # Copiar o dataframe original
        result = df.copy()
        
        # Aplicar filtros se os parâmetros foram fornecidos
        if column_name and search_query:
            if column_name not in df.columns:
                return jsonify({"error": f"Coluna '{column_name}' não encontrada"}), 400
            
            # Filtrar a coluna específica (case insensitive)
            result = result[result[column_name].str.contains(search_query, case=False, na=False)]
        
        elif search_query:  # Busca em todas as colunas se apenas query for fornecida
            mask = result.apply(lambda row: row.astype(str).str.contains(search_query, case=False).any(), axis=1)
            result = result[mask]
        
        # Limitar resultados e converter para JSON
        result = result.head(limit)
        return result.to_json(orient='records', force_ascii=False)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)