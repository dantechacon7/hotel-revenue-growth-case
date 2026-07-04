## Configurando ambiente com DuckDB no colab

!pip install -q duckdb

from google.colab import files

files.upload()

import duckdb

con = duckdb.connect()

## Lendo arquivo
con.sql("""
SELECT *
FROM read_csv_auto('/content/Base Case - base.csv')
LIMIT 10
""").df()

## Gerando tabela fato
con.sql("""
CREATE TABLE fct_hotel_reservations AS
SELECT *
FROM read_csv_auto('/content/Base Case - base.csv')
""")
