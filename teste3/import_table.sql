COPY demo_contabeis(data_lancamento, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'data/1T2023.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demo_contabeis(data_lancamento, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'data/2T2024.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demo_contabeis(data_lancamento, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'data/3T2023.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demo_contabeis(data_lancamento, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'data/4T2023.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demo_contabeis(data_lancamento, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'data/1T2024.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demo_contabeis(data_lancamento, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'data/2T2024.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demo_contabeis(data_lancamento, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'data/3T2024.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY demo_contabeis(data_lancamento, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final)
FROM 'data/4T2024.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

COPY operadoras_saude (cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_de_comercializacao, data_registro_ans)
FROM 'data/Relatorio_cadop.csv'
DELIMITER ';' CSV HEADER ENCODING 'UTF8';

UPDATE operadoras_saude
SET data_registro_ans = TO_DATE(data_registro_ans, 'DD/MM/YYYY');
