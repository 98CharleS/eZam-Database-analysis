import os
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots

# --- Load data ---
df_gdp = pd.read_csv('data/tenders_by_gdp.csv', sep=';', encoding='utf-8-sig')
df_pop = pd.read_csv('data/tenders_by_population.csv', sep=';', encoding='utf-8-sig')
df_split = pd.read_csv('data/tenders_by_population_warsaw_split.csv', sep=';', encoding='utf-8-sig')
df_capita = pd.read_csv('data/tenders_by_gdp_per_capita.csv', sep=';', encoding='utf-8-sig')


# --- Trend line helper ---
def trend_line(x, y):
    coef = np.polyfit(x, y, 1)
    poly = np.poly1d(coef)
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = poly(x_line)
    r = np.corrcoef(x, y)[0, 1]
    r2 = r ** 2
    return x_line, y_line, r, r2


# --- Build subplots: 2 rows ---
fig = make_subplots(
    rows=2, cols=3,
    subplot_titles=(
        'Przetargi vs PKB',
        'Przetargi vs Populacja',
        'Przetargi vs Populacja (z rozbiciem na Warszawę)',
        'PKB vs Populacja województw',
        'Przetargi vs PKB per capita',
        ''
    ),
    vertical_spacing=0.15,
    horizontal_spacing=0.08
)

# --- Chart 1: Tenders vs GDP ---
x1 = df_gdp['gdp_mln_pln']
y1 = df_gdp['total_tenders']
x1_line, y1_line, r1, r2_1 = trend_line(x1, y1)

fig.add_trace(go.Scatter(
    x=x1, y=y1, mode='markers+text', text=df_gdp['wojewodztwo'],
    textposition='top center', textfont=dict(size=8),
    marker=dict(size=8, color='#185FA5'), showlegend=False
), row=1, col=1)

fig.add_trace(go.Scatter(
    x=x1_line, y=y1_line, mode='lines',
    line=dict(color='#D85A30', width=2, dash='dash'),
    name=f'Trend PKB (R²={r2_1:.3f}, r={r1:.3f})'
), row=1, col=1)

# --- Chart 2: Tenders vs Population ---
x2 = df_pop['ludnosc']
y2 = df_pop['total_tenders']
x2_line, y2_line, r2, r2_2 = trend_line(x2, y2)

fig.add_trace(go.Scatter(
    x=x2, y=y2, mode='markers+text', text=df_pop['wojewodztwo'],
    textposition='top center', textfont=dict(size=8),
    marker=dict(size=8, color='#185FA5'), showlegend=False
), row=1, col=2)

fig.add_trace(go.Scatter(
    x=x2_line, y=y2_line, mode='lines',
    line=dict(color='#D85A30', width=2, dash='dash'),
    name=f'Trend pop. (R²={r2_2:.3f}, r={r2:.3f})'
), row=1, col=2)

# --- Chart 3: Tenders vs Population (Warsaw Split) ---
x3 = df_split['ludnosc']
y3 = df_split['total_tenders']
x3_line, y3_line, r3, r2_3 = trend_line(x3, y3)

fig.add_trace(go.Scatter(
    x=x3, y=y3, mode='markers+text', text=df_split['wojewodztwo'],
    textposition='top center', textfont=dict(size=8),
    marker=dict(size=8, color='#185FA5'), showlegend=False
), row=1, col=3)

fig.add_trace(go.Scatter(
    x=x3_line, y=y3_line, mode='lines',
    line=dict(color='#2E8B57', width=2, dash='dash'),
    name=f'Trend split (R²={r2_3:.3f}, r={r3:.3f})'
), row=1, col=3)

# --- Chart 4: GDP vs Population ---
x4 = df_capita['ludnosc']
y4 = df_capita['gdp_mln_pln']
x4_line, y4_line, r4, r2_4 = trend_line(x4, y4)

fig.add_trace(go.Scatter(
    x=x4, y=y4, mode='markers+text', text=df_capita['wojewodztwo'],
    textposition='top center', textfont=dict(size=8),
    marker=dict(size=8, color='#7F77DD'), showlegend=False
), row=2, col=1)

fig.add_trace(go.Scatter(
    x=x4_line, y=y4_line, mode='lines',
    line=dict(color='#D85A30', width=2, dash='dash'),
    name=f'Trend PKB/pop. (R²={r2_4:.3f}, r={r4:.3f})'
), row=2, col=1)

# --- Chart 5: Tenders vs GDP per capita ---
x5 = df_capita['gdp_per_capita_pln']
y5 = df_capita['total_tenders']
x5_line, y5_line, r5, r2_5 = trend_line(x5, y5)

fig.add_trace(go.Scatter(
    x=x5, y=y5, mode='markers+text', text=df_capita['wojewodztwo'],
    textposition='top center', textfont=dict(size=8),
    marker=dict(size=8, color='#185FA5'), showlegend=False
), row=2, col=2)

fig.add_trace(go.Scatter(
    x=x5_line, y=y5_line, mode='lines',
    line=dict(color='#D85A30', width=2, dash='dash'),
    name=f'Trend per capita (R²={r2_5:.3f}, r={r5:.3f})'
), row=2, col=2)

# --- Layout ---
fig.update_layout(
    title=dict(text='Analiza przetargów publicznych w Polsce (2021–2025)', font=dict(size=16)),
    height=900,
    width=1500,
    legend=dict(orientation='h', yanchor='bottom', y=-0.12, xanchor='center', x=0.5),
    plot_bgcolor='white',
    paper_bgcolor='white',
)

# --- Axis labels ---
fig.update_xaxes(title_text='PKB (mln PLN)', row=1, col=1, showgrid=True, gridcolor='#f0f0f0')
fig.update_xaxes(title_text='Populacja', row=1, col=2, showgrid=True, gridcolor='#f0f0f0')
fig.update_xaxes(title_text='Populacja (split)', row=1, col=3, showgrid=True, gridcolor='#f0f0f0')
fig.update_xaxes(title_text='Populacja', row=2, col=1, showgrid=True, gridcolor='#f0f0f0')
fig.update_xaxes(title_text='PKB per capita (PLN)', row=2, col=2, showgrid=True, gridcolor='#f0f0f0')

fig.update_yaxes(title_text='Liczba przetargów', row=1, col=1, showgrid=True, gridcolor='#f0f0f0')
fig.update_yaxes(title_text='Liczba przetargów', row=1, col=2, showgrid=True, gridcolor='#f0f0f0')
fig.update_yaxes(title_text='Liczba przetargów', row=1, col=3, showgrid=True, gridcolor='#f0f0f0')
fig.update_yaxes(title_text='PKB (mln PLN)', row=2, col=1, showgrid=True, gridcolor='#f0f0f0')
fig.update_yaxes(title_text='Liczba przetargów', row=2, col=2, showgrid=True, gridcolor='#f0f0f0')

# --- Save & show ---
os.makedirs('output', exist_ok=True)
fig.write_html('output/tenders_correlation.html')
fig.show()