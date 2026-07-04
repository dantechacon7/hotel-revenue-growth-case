fig, ax = plt.subplots(figsize=(8, 4))
pedidos = [0, 1, 2, 3, '4+']
adr = [74.22, 99.62, 113.13, 139.94, 160]
noites = [3.95, 4.26, 4.49, 5.20, 5.40]
x = np.arange(len(pedidos))
ax.bar(x, adr, color='#3B82F6', label='ADR (R$)')
ax2 = ax.twinx()
ax2.plot(x, noites, color='#EF4444', marker='o', linewidth=2, label='Noites médias')
ax.set_xticks(x); ax.set_xticklabels([f'{p} pedido{"s" if p != 1 else ""}' for p in pedidos])
ax.set_ylabel('ADR (R$)'); ax2.set_ylabel('Noites médias')
ax.set_title('Engajamento — Pedidos Especiais vs ADR e Duração')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1+lines2, labels1+labels2, loc='upper left')
plt.tight_layout()
plt.savefig('grafico_pedidos.png', dpi=150, bbox_inches='tight')
plt.show()
