# config.py — Environment setup and table creation
# IMPORTANT: receita_por_noite uses comma as decimal separator in the CSV.
# Earlier versions of this setup missed this, underestimating revenue ~2.34x.
# This version handles it correctly via pandas str.replace before float cast.

!pip install -q duckdb

from google.colab import files
files.upload()  # upload: Base Case - base.csv

import duckdb
import pandas as pd

df = pd.read_csv('/content/Base Case - base.csv', low_memory=False)
df['receita_por_noite'] = df['receita_por_noite'].astype(str).str.replace(',', '.').astype(float)
df['total_noites'] = df['nro_noites_fds'] + df['nro_noites_dds']
df['receita_total'] = df['receita_por_noite'] * df['total_noites']
df['reserva_cancelada'] = df['reserva_cancelada'].astype(int)

con = duckdb.connect()
con.execute("CREATE TABLE fct_hotel_reservations AS SELECT * FROM df")

# Verify types
con.sql("SELECT typeof(receita_por_noite), typeof(receita_total) FROM fct_hotel_reservations LIMIT 1").df()
