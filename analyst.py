import os
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots

# --- Load data ---
df_gdp = pd.read_csv('data/tenders_by_gdp.csv', sep=';', encoding='utf-8-sig')
df_pop = pd.read_csv('data/tenders_by_population.csv', sep=';', encoding='utf-8-sig')


# --- Trend line helper ---
def trend_line(x, y):
    coef = np.polyfit(x, y, 1)
    poly = np.poly1d(coef)
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = poly(x_line)
    r = np.corrcoef(x, y)[0, 1]
    r2 = r ** 2
    return x_line, y_line, r, r2


# --- Build subplots ---
fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=(
        'Liczba przetargów vs PKB województwa',
        'Liczba przetargów vs Populacja województwa'
    )
)

# --- Chart 1: Tenders vs GDP ---
x1 = df_gdp['gdp_mln_pln']
y1 = df_gdp['total_tenders']
x1_line, y1_line, r1, r2_1 = trend_line(x1, y1)

fig.add_trace(go.Scatter(
    x=x1, y=y1,
    mode='markers+text',
    text=df_gdp['wojewodztwo'],
    textposition='top center',
    textfont=dict(size=9),
    marker=dict(size=8, color='#185FA5'),
    name='Województwa',
    showlegend=False
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=x1_line, y=y1_line,
    mode='lines',
    line=dict(color='#D85A30', width=2, dash='dash'),
    name=f'Trend PKB (R²={r2_1:.3f}, r={r1:.3f})',
    showlegend=True
), row=1, col=1)

# --- Chart 2: Tenders vs Population ---
x2 = df_pop['ludnosc']
y2 = df_pop['total_tenders']
x2_line, y2_line, r2, r2_2 = trend_line(x2, y2)

fig.add_trace(go.Scatter(
    x=x2, y=y2,
    mode='markers+text',
    text=df_pop['wojewodztwo'],
    textposition='top center',
    textfont=dict(size=9),
    marker=dict(size=8, color='#185FA5'),
    name='Województwa',
    showlegend=False
), row=1, col=2)

fig.add_trace(go.Scatter(
    x=x2_line, y=y2_line,
    mode='lines',
    line=dict(color='#D85A30', width=2, dash='dash'),
    name=f'Trend populacja (R²={r2_2:.3f}, r={r2:.3f})',
    showlegend=True
), row=1, col=2)

# --- Layout ---
fig.update_layout(
    title=dict(text='Analiza przetargów publicznych w Polsce (2021–2025)', font=dict(size=16)),
    height=550,
    legend=dict(orientation='h', yanchor='bottom', y=-0.2, xanchor='center', x=0.5),
    plot_bgcolor='white',
    paper_bgcolor='white',
)

fig.update_xaxes(title_text='PKB (mln PLN)', row=1, col=1, showgrid=True, gridcolor='#f0f0f0')
fig.update_xaxes(title_text='Populacja', row=1, col=2, showgrid=True, gridcolor='#f0f0f0')
fig.update_yaxes(title_text='Liczba przetargów', row=1, col=1, showgrid=True, gridcolor='#f0f0f0')
fig.update_yaxes(title_text='Liczba przetargów', row=1, col=2, showgrid=True, gridcolor='#f0f0f0')

# --- Save & show ---
os.makedirs('output', exist_ok=True)
fig.write_html('output/tenders_correlation.html')
fig.show()