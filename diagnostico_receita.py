import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Diagnóstico de Receita — Hotel', fontsize=14, fontweight='bold')

# 1. Cancelamento por antecedência
ax1 = axes[0, 0]
faixas = ['0–7 dias', '8–30 dias', '31–90 dias', '90+ dias']
pct_canc = [6.48, 21.95, 32.46, 39.44]
receita_perdida = [72771, 386395, 907064, 1888594]
bars = ax1.bar(faixas, pct_canc, color='#3B82F6')
ax2_twin = ax1.twinx()
ax2_twin.plot(faixas, receita_perdida, color='#EF4444', marker='o', linewidth=2)
ax2_twin.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R${x/1e3:.0f}k'))
ax1.set_ylabel('% Cancelamento')
ax2_twin.set_ylabel('Receita Perdida')
ax1.set_title('Cancelamento por Antecedência')
ax1.set_ylim(0, 55)

# 2. Receita + cancelamento por canal
ax2 = axes[0, 1]
canais = ['AT Online', 'Direta', 'AT Offline', 'Grupos', 'Corporativo']
receitas = [2340453, 1208774, 657623, 584721, 176041]
canc = [35.24, 13.48, 15.23, 42.39, 15.20]
x = np.arange(len(canais))
ax2.bar(x, receitas, color='#3B82F6', label='Receita')
ax3_twin = ax2.twinx()
ax3_twin.plot(x, canc, color='#EF4444', marker='o', linewidth=2, label='% Cancel.')
ax2.set_xticks(x); ax2.set_xticklabels(canais, rotation=20, ha='right')
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R${x/1e6:.1f}M'))
ax3_twin.set_ylabel('% Cancelamento')
ax2.set_title('Receita e Cancelamento por Canal')

# 3. ADR por tipo de quarto
ax3 = axes[1, 0]
quartos = ['A', 'D', 'E', 'F', 'G', 'H']
adr = [73.69, 107.59, 118.67, 134.16, 169.84, 190.24]
pct_q = [27.32, 26.33, 28.39, 16.31, 40.07, 40.90]
bars3 = ax3.bar(quartos, adr, color='#3B82F6')
ax4_twin = ax3.twinx()
ax4_twin.plot(quartos, pct_q, color='#EF4444', marker='o', linewidth=2)
ax3.set_ylabel('ADR (R$)')
ax4_twin.set_ylabel('% Cancelamento')
ax3.set_title('ADR e Cancelamento por Tipo de Quarto')

# 4. Sazonalidade de receita
ax4 = axes[1, 1]
meses_labels = ['Jul/15','Ago/15','Set/15','Out/15','Nov/15','Dez/15',
                'Jan/16','Fev/16','Mar/16','Abr/16','Mai/16','Jun/16',
                'Jul/16','Ago/16','Set/16','Out/16','Nov/16','Dez/16',
                'Jan/17','Fev/17','Mar/17','Abr/17','Mai/17','Jun/17','Jul/17','Ago/17']
receitas_mes = [261242,346747,162870,91978,93661,55912,
                55576,105880,142542,139076,167018,172881,
                299290,429788,241032,188397,76762,106715,
                103708,126090,172500,212872,198040,242785,361743,412507]
ax4.plot(range(len(meses_labels)), receitas_mes, color='#3B82F6', linewidth=2, marker='.')
ax4.fill_between(range(len(meses_labels)), receitas_mes, alpha=0.2, color='#3B82F6')
ax4.set_xticks(range(0, len(meses_labels), 3))
ax4.set_xticklabels(meses_labels[::3], rotation=30, ha='right')
ax4.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'R${x/1e3:.0f}k'))
ax4.set_title('Sazonalidade de Receita (2015–2017)')

# 5. forma de pagamento vs cancelamento

fig2, ax5 = plt.subplots(figsize=(6, 4))
pgto = ['Sem pgto', 'Pgto reembolsável', 'Pgto não reembolsável*']
pct_pgto = [24.78, 15.49, 95.99]
cores = ['#3B82F6', '#3B82F6', '#EF4444']
ax5.barh(pgto, pct_pgto, color=cores)
ax5.set_xlabel('% Cancelamento')
ax5.set_title('Cancelamento por Forma de Pagamento')
ax5.set_xlim(0, 110)
for i, v in enumerate(pct_pgto):
    ax5.text(v + 1, i, f'{v}%', va='center')
fig2.tight_layout()
fig2.savefig('grafico_pagamento.png', dpi=150, bbox_inches='tight')
plt.show()

plt.tight_layout()
plt.savefig('graficos_hotel.png', dpi=150, bbox_inches='tight')
plt.show()
