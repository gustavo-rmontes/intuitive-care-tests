<template>
  <div class="api-search-component">
    <h2>Pesquisa de Operadoras de Saúde</h2>

    <div class="search-form">
      <div class="form-group">
        <label for="column">Coluna:</label>
        <select id="column" v-model="searchParams.column" class="form-control">
          <option value="">Todas as colunas</option>
          <option v-for="column in availableColumns" :key="column.value" :value="column.value">
            {{ column.label }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label for="query">Termo de busca:</label>
        <input id="query" type="text" v-model="searchParams.query" class="form-control"
          placeholder="Digite o termo de busca" @keyup.enter="search">
      </div>

      <div class="form-group">
        <label for="limit">Limite de resultados:</label>
        <input id="limit" type="number" v-model.number="searchParams.limit" class="form-control" min="1" max="100">
      </div>

      <button @click="search" class="btn btn-primary" :disabled="loading">
        <span v-if="loading">
          <i class="fas fa-spinner fa-spin"></i> Buscando...
        </span>
        <span v-else>
          <i class="fas fa-search"></i> Buscar
        </span>
      </button>
    </div>

    <div v-if="error" class="alert alert-danger">
      <i class="fas fa-exclamation-triangle"></i> {{ error }}
    </div>

    <div v-if="results.length > 0" class="results-container">
      <div class="results-header">
        <h3>Resultados ({{ results.length }})</h3>
        <button @click="exportToCSV" class="btn btn-export">
          <i class="fas fa-file-csv"></i> Exportar CSV
        </button>
      </div>

      <div class="table-responsive">
        <table class="results-table">
          <thead>
            <tr>
              <th v-for="column in displayedColumns" :key="column">
                {{ formatColumnName(column) }}
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in results" :key="index">
              <td v-for="column in displayedColumns" :key="column">
                {{ formatValue(item[column]) }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div v-if="results.length >= searchParams.limit" class="results-limit">
        Mostrando apenas os primeiros {{ searchParams.limit }} resultados
      </div>
    </div>

    <div v-else-if="searched" class="no-results">
      <i class="fas fa-info-circle"></i> Nenhum resultado encontrado.
    </div>
  </div>
</template>

<script>
export default {
  name: 'HealthOperatorSearch',
  data() {
    return {
      searchParams: {
        column: '',
        query: '',
        limit: 10
      },
      results: [],
      loading: false,
      error: null,
      searched: false,
      baseUrl: 'http://localhost:8080/search',
      availableColumns: [
        { value: 'Razao_Social', label: 'Razão Social' },
        { value: 'Nome_Fantasia', label: 'Nome Fantasia' },
        { value: 'CNPJ', label: 'CNPJ' },
        { value: 'Registro_ANS', label: 'Registro ANS' },
        { value: 'Modalidade', label: 'Modalidade' },
        { value: 'Cidade', label: 'Cidade' },
        { value: 'UF', label: 'UF' },
        { value: 'Telefone', label: 'Telefone' },
        { value: 'Endereco_eletronico', label: 'E-mail' }
      ],
      displayedColumns: [
        'Registro_ANS',
        'CNPJ',
        'Razao_Social',
        'Nome_Fantasia',
        'Modalidade',
        'Cidade',
        'UF',
        'Telefone'
      ]
    }
  },
  methods: {
    async search() {
      this.loading = true;
      this.error = null;

      try {
        const params = new URLSearchParams();
        if (this.searchParams.column) params.append('column', this.searchParams.column);
        if (this.searchParams.query) params.append('query', this.searchParams.query);
        params.append('limit', this.searchParams.limit);

        const response = await fetch(`${this.baseUrl}?${params.toString()}`, {
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          mode: 'cors'
        });

        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

        const data = await response.json();
        console.log('Dados recebidos:', data); // Adicione para debug

        this.results = Array.isArray(data) ? data : [data];
        this.searched = true;

      } catch (err) {
        console.error('Erro completo:', err);
        this.error = `Falha na busca: ${err.message}`;
        this.results = [];
      } finally {
        this.loading = false;
      }
    },

    formatColumnName(column) {
      const columnNames = {
        'Registro_ANS': 'Registro ANS',
        'Razao_Social': 'Razão Social',
        'Nome_Fantasia': 'Nome Fantasia',
        'Endereco_eletronico': 'E-mail',
        'Data_Registro_ANS': 'Data Registro'
      };
      return columnNames[column] || column.replace(/_/g, ' ');
    },

    formatValue(value) {
      if (value === null || value === undefined) return '-';

      // Formatar CNPJ
      if (/^\d{14}$/.test(value)) {
        return value.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, '$1.$2.$3/$4-$5');
      }

      // Remover caracteres especiais de encoding
      if (typeof value === 'string') {
        return value.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
      }

      return value;
    },

    exportToCSV() {
      if (this.results.length === 0) return;

      let csv = '';

      // Cabeçalho
      csv += this.displayedColumns.map(col => `"${this.formatColumnName(col)}"`).join(';') + '\n';

      // Dados
      this.results.forEach(item => {
        const row = this.displayedColumns.map(col => {
          let value = item[col] || '';
          if (typeof value === 'string') {
            value = value.replace(/"/g, '""'); // Escape aspas
            return `"${value}"`;
          }
          return value;
        });
        csv += row.join(';') + '\n';
      });

      // Criar e baixar arquivo
      const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      const link = document.createElement('a');
      const url = URL.createObjectURL(blob);

      link.setAttribute('href', url);
      link.setAttribute('download', `operadoras_${new Date().toISOString().slice(0, 10)}.csv`);
      link.style.visibility = 'hidden';

      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  }
}
</script>

<style scoped>
.api-search-component {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.search-form {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 15px;
  margin-bottom: 25px;
  align-items: end;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-control {
  padding: 8px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
  height: 38px;
}

label {
  margin-bottom: 5px;
  font-weight: 600;
  font-size: 14px;
  color: #555;
}

.btn {
  padding: 8px 16px;
  background-color: #2c7be5;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.btn:hover {
  background-color: #1a68d1;
}

.btn:disabled {
  background-color: #95a9c9;
  cursor: not-allowed;
}

.btn-export {
  background-color: #27b08a;
}

.btn-export:hover {
  background-color: #1e9974;
}

.alert {
  padding: 12px 15px;
  border-radius: 4px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 10px;
}

.alert-danger {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

.results-container {
  margin-top: 25px;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  overflow: hidden;
}

.results-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 20px;
  background-color: #f8f9fa;
  border-bottom: 1px solid #e0e0e0;
}

.results-header h3 {
  margin: 0;
  font-size: 18px;
  color: #333;
}

.table-responsive {
  overflow-x: auto;
}

.results-table {
  width: 100%;
  border-collapse: collapse;
}

.results-table th,
.results-table td {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #e0e0e0;
}

.results-table th {
  background-color: #f1f3f5;
  font-weight: 600;
  color: #495057;
  white-space: nowrap;
}

.results-table tr:hover {
  background-color: #f8f9fa;
}

.results-table td {
  color: #495057;
  vertical-align: top;
}

.no-results {
  margin-top: 20px;
  padding: 15px;
  background-color: #f8f9fa;
  border-radius: 4px;
  color: #6c757d;
  display: flex;
  align-items: center;
  gap: 10px;
}

.results-limit {
  padding: 10px 15px;
  background-color: #fff3cd;
  color: #856404;
  font-size: 14px;
  text-align: center;
}

.fa-spinner {
  animation: fa-spin 1s infinite linear;
}

@keyframes fa-spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>