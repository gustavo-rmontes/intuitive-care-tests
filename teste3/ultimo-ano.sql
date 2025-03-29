WITH ultimos_12_meses AS
    ( SELECT d.reg_ans,
             o.razao_social,
             SUM(d.vl_saldo_final) AS total_despesas
     FROM demo_contabeis d
     JOIN operadoras_saude o ON d.reg_ans = o.reg_ans
     WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
         AND d.data_lancamento >= (CURRENT_DATE - INTERVAL '12 months')
     GROUP BY d.reg_ans,
              o.razao_social)
SELECT *
FROM ultimos_12_meses
ORDER BY total_despesas DESC
LIMIT 10;