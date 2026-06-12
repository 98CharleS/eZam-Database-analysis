import os
import sys
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from statsmodels.tsa.seasonal import STL
import matplotlib
matplotlib.use('Agg')              # render PNG bez przeglądarki (kaleido bywa zawodne)
import matplotlib.pyplot as plt

MONTHS_PL = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze',
             'Lip', 'Sie', 'Wrz', 'Paź', 'Lis', 'Gru']

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Minimalny wolumen działu, poniżej którego współczynniki sezonowości są zbyt
# zaszumione, by je interpretować (np. maszyny górnicze ~2000 przetargów/5 lat).
MIN_TOTAL = 2000
INDEX_START = '2022-01-01'      # indeksy sezonowe liczone bez rozpędzania 2021
PROFILE_DIVS = [60, 64, 90, 31, 80]   # działy pokazane na wykresie profili

# --- Wczytanie i pełna siatka miesięcy × dział ---
df = pd.read_csv('data/tenders_by_month_and_division.csv', sep=';', encoding='utf-8')
df['month'] = pd.to_datetime(df['month'] + '-01')
names = df.drop_duplicates('cpv_division').set_index('cpv_division')['division_name'].to_dict()

piv = (df.pivot_table(index='month', columns='cpv_division',
                      values='tender_count', aggfunc='sum')
         .reindex(pd.date_range('2021-01-01', '2025-12-01', freq='MS'))
         .fillna(0))

# --- Współczynniki sezonowości dla każdego działu ---
rows = []
profiles = {}
for div in piv.columns:
    s = piv[div]
    total = int(s.sum())
    if total < MIN_TOTAL:
        continue

    # Indeks sezonowy 2022-2025 (100 = przeciętny miesiąc), metoda ratio-to-mean
    si = s[INDEX_START:]
    month_mean = si.groupby(si.index.month).mean()
    index = (month_mean / month_mean.mean() * 100).reindex(range(1, 13))
    profiles[div] = index

    amp = index.max() / index.min()                 # szczyt/dołek
    cv = index.std(ddof=0) / index.mean() * 100      # współczynnik zmienności
    peak, trough = int(index.idxmax()), int(index.idxmin())

    # Siła sezonowości STL na pełnym zakresie 2021-2025
    res = STL(s, period=12, robust=True).fit()
    fs = max(0.0, 1 - res.resid.var() / (res.seasonal + res.resid).var())

    rows.append({'division': div, 'name': names[div], 'total': total,
                 'Fs': round(fs, 3), 'amplitude': round(amp, 2),
                 'cv_pct': round(cv, 1),
                 'peak': MONTHS_PL[peak - 1], 'trough': MONTHS_PL[trough - 1]})

res_df = pd.DataFrame(rows).sort_values('Fs', ascending=False).reset_index(drop=True)

# --- Konsola ---
print(f'=== Sezonowość per dział (n >= {MIN_TOTAL}; {len(res_df)} działów) ===')
print('Indeksy: 2022-2025 | STL/Fs: 2021-2025')
print(res_df.to_string(index=False))

# --- Zapis współczynników ---
os.makedirs('output', exist_ok=True)
res_df.to_csv('output/seasonality_by_division.csv', sep=';',
              index=False, encoding='utf-8-sig')

# --- Wykres: ranking siły sezonowości + profile wybranych działów ---
fig = make_subplots(
    rows=1, cols=2, column_widths=[0.46, 0.54], horizontal_spacing=0.12,
    subplot_titles=(
        f'Siła sezonowości działów (STL, Fs) — {len(res_df)} działów (n ≥ {MIN_TOTAL})',
        'Profile sezonowe wybranych działów (indeks 2022–2025, 100 = przeciętny miesiąc)'
    ))

# Lewy panel: poziomy ranking Fs (od najsłabszego u dołu do najsilniejszego u góry)
rank = res_df.sort_values('Fs')
labels = [f"{r.division} {r['name']}" for _, r in rank.iterrows()]
fig.add_trace(go.Bar(
    x=rank['Fs'], y=labels, orientation='h',
    marker=dict(color=rank['Fs'], colorscale='YlGnBu', cmin=0, cmax=1,
                line=dict(width=0)),
    text=rank['Fs'].map('{:.2f}'.format), textposition='outside',
    showlegend=False), row=1, col=1)

# Prawy panel: profile sezonowe kilku reprezentatywnych działów
palette = ['#185FA5', '#2E8B57', '#D85A30', '#8E44AD', '#C2A100']
for color, div in zip(palette, PROFILE_DIVS):
    if div not in profiles:
        continue
    fig.add_trace(go.Scatter(
        x=MONTHS_PL, y=profiles[div].values, mode='lines+markers',
        name=f'{div} {names[div]}', line=dict(color=color, width=2.5)),
        row=1, col=2)
fig.add_hline(y=100, line_dash='dash', line_color='#888', row=1, col=2)

fig.update_layout(
    title=dict(text='Sezonowość przetargów publicznych w podziale na działy CPV (2021–2025)',
               font=dict(size=16)),
    height=900, width=1500, plot_bgcolor='white', paper_bgcolor='white',
    legend=dict(orientation='h', yanchor='bottom', y=-0.12, xanchor='right', x=1))
fig.update_xaxes(title_text='Siła sezonowości Fs', range=[0, 1.08], row=1, col=1,
                 gridcolor='#f0f0f0')
fig.update_yaxes(tickfont=dict(size=9), row=1, col=1)
fig.update_yaxes(title_text='Indeks sezonowy', row=1, col=2, gridcolor='#f0f0f0')
fig.update_xaxes(gridcolor='#f0f0f0', row=1, col=2)

fig.write_html('output/seasonality_by_division.html')

# --- Statyczny PNG do report.md (matplotlib, bez przeglądarki) ---
rank = res_df.sort_values('Fs')
labels = [f"{int(r.division)} {r['name']}" for _, r in rank.iterrows()]
mfig, (axL, axR) = plt.subplots(
    1, 2, figsize=(15, 9), gridspec_kw={'width_ratios': [0.46, 0.54]})

bar_colors = plt.cm.YlGnBu(np.clip(rank['Fs'].values, 0, 1))
axL.barh(range(len(rank)), rank['Fs'], color=bar_colors)
axL.set_yticks(range(len(rank)))
axL.set_yticklabels(labels, fontsize=8)
axL.set_ylim(-0.6, len(rank) - 0.4)
axL.set_xlim(0, 1.1)
axL.set_xlabel('Siła sezonowości Fs')
for i, v in enumerate(rank['Fs']):
    axL.text(v + 0.012, i, f'{v:.2f}', va='center', fontsize=7, color='#333')
axL.set_title(f'Siła sezonowości działów (STL, Fs) — {len(res_df)} działów (n ≥ {MIN_TOTAL})',
              fontsize=11)
axL.grid(axis='x', color='#eee')
axL.set_axisbelow(True)

palette = ['#185FA5', '#2E8B57', '#D85A30', '#8E44AD', '#C2A100']
for color, div in zip(palette, PROFILE_DIVS):
    if div in profiles:
        axR.plot(MONTHS_PL, profiles[div].values, marker='o', color=color,
                 linewidth=2.3, label=f'{div} {names[div]}')
axR.axhline(100, linestyle='--', color='#888', linewidth=1)
axR.set_ylabel('Indeks sezonowy')
axR.set_title('Profile sezonowe wybranych działów (2022–2025, 100 = przeciętny miesiąc)',
              fontsize=11)
axR.legend(fontsize=8, loc='upper left')
axR.grid(color='#eee')
axR.set_axisbelow(True)

mfig.suptitle('Sezonowość przetargów publicznych w podziale na działy CPV (2021–2025)',
              fontsize=14)
mfig.tight_layout(rect=[0, 0, 1, 0.97])
mfig.savefig('output/seasonality_by_division.png', dpi=150)

print('\nZapisano: output/seasonality_by_division.png, .html, '
      'output/seasonality_by_division.csv')
