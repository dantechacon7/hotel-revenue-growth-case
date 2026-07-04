data = [
    ['1', 'Depósito >30 dias (exceto Grupos)', '~R$ 200k', 'Baixo', 'Imediato'],
    ['2', 'Upsell quarto + pedidos pré-chegada', '~R$ 180k', 'Baixo', 'Imediato'],
    ['', 'Subtotal imediato', '~R$ 380k (38%)', '—', '—'],
    ['3', 'Retenção D-60/D-30 (showcase)', '~R$ 100k', 'Médio', '1–2 meses'],
    ['5', 'Pacotes baixa temporada', '~R$ 100k', 'Médio', '1–2 meses'],
    ['', 'Subtotal curto prazo', '~R$ 580k (58%)', '—', '—'],
    ['4', 'Migração canal Direto', '~R$ 150k', 'Médio', '3–6 meses'],
    ['6', 'Contratos corporativos', '~R$ 60k', 'Médio', '3–6 meses'],
    ['', 'Subtotal médio prazo', '~R$ 790k (79%)', '—', '—'],
    ['7', 'Programa fidelização', '~R$ 80k', 'Alto', '6–12 meses'],
    ['', 'Total acumulado', '~R$ 870k (87%)', '—', '—'],
]
cols = ['#', 'Iniciativa', 'Impacto Est.', 'Esforço', 'Prazo']
subtotal_rows = {2, 5, 8, 10}

fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')
table = ax.table(cellText=data, colLabels=cols, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(9)
table.auto_set_column_width([0,1,2,3,4])

for j in range(5):
    table[0,j].set_facecolor('#16428A')
    table[0,j].set_text_props(color='white', fontweight='bold')

for i in range(1, len(data)+1):
    if (i-1) in subtotal_rows:
        for j in range(5):
            table[i,j].set_facecolor('#DBEAFE')
            table[i,j].set_text_props(fontweight='bold')
    else:
        bg = '#EFF6FF' if i % 2 == 0 else 'white'
        for j in range(5):
            table[i,j].set_facecolor(bg)

plt.tight_layout()
plt.savefig('quadro_priorizacao.png', dpi=150, bbox_inches='tight')
plt.show()
