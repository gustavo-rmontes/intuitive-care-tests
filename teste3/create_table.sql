CREATE TABLE demo_contabeis (
    id SERIAL PRIMARY KEY, 
    data_lancamento DATE NOT NULL, 
    reg_ans VARCHAR(10) NOT NULL,   
    cd_conta_contabil VARCHAR(20) NOT NULL,  
    descricao TEXT NOT NULL,
    vl_saldo_inicial DECIMAL(18,2) NOT NULL,
    vl_saldo_final DECIMAL(18,2) NOT NULL
);

CREATE TABLE operadoras_saude (
    id SERIAL PRIMARY KEY,
    cnpj VARCHAR(14) NOT NULL,  
    razao_social TEXT NOT NULL,
    nome_fantasia TEXT,
    modalidade TEXT NOT NULL,
    logradouro TEXT NOT NULL,
    numero VARCHAR(10),  
    complemento TEXT,
    bairro TEXT NOT NULL,
    cidade TEXT NOT NULL,
    uf CHAR(2) NOT NULL,
    cep VARCHAR(8) NOT NULL,  
    ddd VARCHAR(2) NOT NULL, 
    telefone VARCHAR(11),  
    fax VARCHAR(11),
    endereco_eletronico TEXT,
    representante TEXT NOT NULL,
    cargo_representante TEXT NOT NULL,
    regiao_de_comercializacao INT NOT NULL,
    data_registro_ans DATE NOT NULL
);
