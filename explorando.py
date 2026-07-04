# Visão geral de volumetrias importantes
con.sql("""
SELECT
  COUNT(*) AS total_reservas,
  SUM(CASE WHEN reserva_cancelada=1 THEN 1 ELSE 0 END) AS canceladas,
  ROUND(AVG(reserva_cancelada)*100,2) AS pct_cancelamento,
  ROUND(SUM(CASE WHEN reserva_cancelada=0 THEN receita_total END),2) AS receita_realizada,
  ROUND(SUM(CASE WHEN reserva_cancelada=1 THEN receita_total END),2) AS receita_perdida_cancelamento,
  ROUND(AVG(CASE WHEN reserva_cancelada=0 THEN receita_por_noite END),2) AS adr_medio
FROM fct_hotel_reservations
""").show()

# Cancelamento por faixa de antecedência
con.sql("""
SELECT
CASE WHEN tempo_antecedencia<=7 THEN '0-7'
WHEN tempo_antecedencia<=30 THEN '8-30'
WHEN tempo_antecedencia<=90 THEN '31-90'
ELSE '90+' END AS faixa,
COUNT(*) n,
ROUND(AVG(reserva_cancelada)*100,2) pct_canc,
ROUND(SUM(CASE WHEN reserva_cancelada=1 THEN receita_total END),2) receita_perdida
FROM fct_hotel_reservations
GROUP BY 1
ORDER BY 1
""").df()

# Cancelamento e ADR por segmento de mercado
con.sql("""
SELECT
  segmento_mercado,
  COUNT(*) AS total_reservas,
  ROUND(AVG(reserva_cancelada)*100,2) AS pct_cancelamento,
  ROUND(AVG(receita_por_noite),2) AS adr_medio,
  ROUND(SUM(CASE WHEN reserva_cancelada=0 THEN receita_total END),2) AS receita_realizada
FROM fct_hotel_reservations
GROUP BY 1
ORDER BY receita_realizada DESC
""").show()

# Sazonalidade mensal (ocupação e receita)
con.sql("""
SELECT
  ano_chegada, mes_chegada,
  COUNT(*) AS total_reservas,
  ROUND(AVG(reserva_cancelada)*100,2) AS pct_cancelamento,
  ROUND(SUM(CASE WHEN reserva_cancelada=0 THEN receita_total END),2) AS receita_realizada
FROM fct_hotel_reservations
GROUP BY 1,2
ORDER BY 1,2
""").show()

# Forma de pagamento vs cancelamento
con.sql("""
SELECT
  tipo_pgto,
  COUNT(*) AS total_reservas,
  ROUND(AVG(reserva_cancelada)*100,2) AS pct_cancelamento
FROM fct_hotel_reservations
GROUP BY 1
ORDER BY pct_cancelamento DESC
""").show()

# Duração de estadia e ADR por tipo de quarto
con.sql("""
SELECT
  tipo_quarto,
  COUNT(*) AS total_reservas,
  ROUND(AVG(total_noites),2) AS media_noites,
  ROUND(AVG(receita_por_noite),2) AS adr_medio,
  ROUND(AVG(reserva_cancelada)*100,2) AS pct_cancelamento
FROM fct_hotel_reservations
GROUP BY 1
ORDER BY total_reservas DESC
""").show()

# Cliente recorrente: retenção e valor
con.sql("""
SELECT
  cliente_recorrente,
  COUNT(*) AS total_reservas,
  ROUND(AVG(reserva_cancelada)*100,2) AS pct_cancelamento,
  ROUND(AVG(receita_por_noite),2) AS adr_medio,
  ROUND(AVG(total_noites),2) AS media_noites
FROM fct_hotel_reservations
GROUP BY 1
""").show()

# países top 10
con.sql("""
SELECT
país,
COUNT(*) n,
ROUND(AVG(reserva_cancelada)*100,2) pct_canc,
ROUND(AVG(receita_por_noite),2) adr
FROM fct_hotel_reservations
GROUP BY 1
ORDER BY n DESC
LIMIT 10
""").df()

# alimentação vs ADR e cancelamento
con.sql("""
SELECT alimentacao,
COUNT(*) n,
ROUND(AVG(reserva_cancelada)*100,2) pct_canc,
ROUND(AVG(receita_por_noite),2) adr
FROM fct_hotel_reservations
GROUP BY 1
ORDER BY n DESC
""").df()

# cancelamento de 95.99% em reservas de pgto não reembolsável - entender se há algum padrão
con.sql("""
SELECT
  segmento_mercado,
  CASE WHEN tempo_antecedencia<=7 THEN '0-7' WHEN tempo_antecedencia<=30 THEN '8-30'
       WHEN tempo_antecedencia<=90 THEN '31-90' ELSE '90+' END faixa_antecedencia,
  tipo_quarto,
  país,
  COUNT(*) n,
  SUM(reserva_cancelada) canceladas,
  ROUND(AVG(reserva_cancelada)*100,2) pct_canc,
  ROUND(AVG(receita_por_noite),2) adr
FROM fct_hotel_reservations
WHERE tipo_pgto = 'Pgto não reembolsável'
GROUP BY ALL
ORDER BY n DESC
LIMIT 20
""").df()

# status por ADR pra investigar os casos não reembolsáveis

con.sql("""
SELECT status_reserva,
COUNT(*) n,
ROUND(AVG(receita_por_noite),2) adr
FROM fct_hotel_reservations
WHERE tipo_pgto = 'Pgto não reembolsável'
GROUP BY 1
ORDER BY n DESC
""").df()

# confirmando se jul é um pico puxado por Portugal
con.sql("""
SELECT
mes_chegada,
COUNT(*)
FROM fct_hotel_reservations
WHERE reserva_cancelada=0
AND país='PRT'
GROUP BY 1
ORDER BY 1""").df()

# quais canais sustentam determinadas sazonalidades?
con.sql("""
SELECT
mes_chegada,
segmento_mercado,
COUNT(*)
FROM fct_hotel_reservations
WHERE reserva_cancelada=0
GROUP BY 1,2
ORDER BY 1,2""").df()

# pedidos especiais e engajamento
con.sql("""
SELECT
pedidos_especiais,
mes_chegada,
COUNT(*),
ROUND(AVG(receita_por_noite),2),
ROUND(AVG(total_noites),2)
FROM fct_hotel_reservations
WHERE reserva_cancelada=0
GROUP BY 1,2 ORDER BY 1""").df()
