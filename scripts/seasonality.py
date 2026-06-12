import os
import sys
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from statsmodels.tsa.seasonal import STL

MONTHS_PL = ['Sty', 'Lut', 'Mar', 'Kwi', 'Maj', 'Cze',
             'Lip', 'Sie', 'Wrz', 'Paź', 'Lis', 'Gru']
WEEKDAYS_PL = ['Pon', 'Wt', 'Śr', 'Czw', 'Pt', 'Sob', 'Nie']

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# --- Load daily series and fill the gaps (missing days = 0 tenders) ---
df = pd.read_csv('data/tenders_by_day.csv', sep=';', encoding='utf-8-sig')
df['publication_date'] = pd.to_datetime(df['publication_date'])
daily = (df.set_index('publication_date')['tender_count']
           .asfreq('D')            # reindex to a complete calendar
           .fillna(0)              # absent days had no publications
           .astype(int))

# 2021 is the data-collection ramp-up (Jan 2021 ~15 tenders/day vs ~175-218 in later
# Januaries), which distorts the seasonal profile. Indices use the four clean full years;
# the trend/STL chart below keeps the full 2021-2025 history (the growth is real adoption).
INDEX_START = '2022-01-01'
daily_idx = daily[INDEX_START:]

# --- Monthly seasonal indices (ratio-to-annual-mean method) ---
# Work on mean tenders per day within each month to remove the month-length bias,
# then express each month relative to its own year's average to remove the trend.
md = daily_idx.to_frame('count')
md['year'] = md.index.year
md['month'] = md.index.month
month_mean = md.groupby(['year', 'month'])['count'].mean()           # avg/day per (year, month)
year_mean = month_mean.groupby('year').transform('mean')             # that year's baseline
ratios = (month_mean / year_mean).groupby('month').mean()            # avg ratio per calendar month
month_index = (ratios / ratios.mean() * 100).reindex(range(1, 13))   # normalise so mean = 100

# --- Day-of-week indices ---
dow_mean = daily_idx.groupby(daily_idx.index.dayofweek).mean()
dow_index = (dow_mean / dow_mean.mean() * 100).reindex(range(7))

# --- STL decomposition on monthly totals (period = 12) ---
monthly_total = daily.resample('MS').sum()
stl = STL(monthly_total, period=12, robust=True).fit()
trend, seasonal, resid = stl.trend, stl.seasonal, stl.resid
# Strength of trend / seasonality (Wang, Smith & Hyndman): share of de-seasonalised /
# de-trended variance explained by the component. Both in [0, 1].
trend_strength = max(0.0, 1 - resid.var() / (trend + resid).var())
seasonal_strength = max(0.0, 1 - resid.var() / (seasonal + resid).var())

# --- Linear trend on the clean window (2022-2025), analogous to the correlation section ---
mt_clean = monthly_total[INDEX_START:]
x = np.arange(len(mt_clean))
slope, intercept = np.polyfit(x, mt_clean.values, 1)
r_trend = np.corrcoef(x, mt_clean.values)[0, 1]
r2_trend = r_trend ** 2

# --- Seasonal amplitude of the monthly index ---
amp_ratio = month_index.max() / month_index.min()          # peak-to-trough ratio
cv_month = month_index.std(ddof=0) / month_index.mean()    # coefficient of variation

# --- Console summary ---
print('=== Sezonowość przetargów (cały zbiór) ===')
print(f'Trend/STL: 2021-2025 | Indeksy sezonowe: 2022-2025 (2021 = rozpędzanie zbioru, pominięte)')
print(f'Dni w kalendarzu: {len(daily)} | dni z publikacjami: {int((daily > 0).sum())} '
      f'| suma przetargów: {int(daily.sum()):,}'.replace(',', ' '))
print('\n--- Współczynniki ---')
print(f'Siła trendu (STL, 2021-2025):      Ft = {trend_strength:.3f}')
print(f'Siła sezonowości (STL, 2021-2025): Fs = {seasonal_strength:.3f}')
print(f'Trend liniowy 2022-2025: r = {r_trend:.3f}, R² = {r2_trend:.3f}, '
      f'nachylenie = {slope:+.0f} przet./mies. ({slope*12:+.0f}/rok)')
print(f'Amplituda sezonowa: szczyt/dołek = {amp_ratio:.2f}× | CV indeksu = {cv_month*100:.1f}%')

print('\nIndeksy miesięczne 2022-2025 (100 = miesiąc przeciętny):')
for m in range(1, 13):
    val = month_index.loc[m]
    print(f'  {MONTHS_PL[m-1]}: {val:6.1f}  {"+" if val >= 100 else "-"}{abs(val-100):4.1f}%')
peak_m, low_m = month_index.idxmax(), month_index.idxmin()
print(f'  -> szczyt: {MONTHS_PL[peak_m-1]} ({month_index.loc[peak_m]:.1f}), '
      f'dołek: {MONTHS_PL[low_m-1]} ({month_index.loc[low_m]:.1f})')

print('\nIndeksy dnia tygodnia 2022-2025 (100 = dzień przeciętny):')
for d in range(7):
    print(f'  {WEEKDAYS_PL[d]}: {dow_index.loc[d]:6.1f}')

# --- Save indices to CSV ---
os.makedirs('output', exist_ok=True)
pd.DataFrame({'month': range(1, 13),
              'month_name': MONTHS_PL,
              'seasonal_index': month_index.values.round(2)}
             ).to_csv('output/seasonality_monthly_index.csv', sep=';',
                      index=False, encoding='utf-8-sig')

# --- Interactive figure ---
fig = make_subplots(
    rows=2, cols=2,
    specs=[[{'colspan': 2}, None], [{}, {}]],
    subplot_titles=(
        f'Dekompozycja STL miesięcznych wolumenów 2021–2025 (siła sezonowości = {seasonal_strength:.2f})',
        'Indeks sezonowości miesięcznej 2022–2025 (100 = przeciętny miesiąc)',
        'Indeks dnia tygodnia 2022–2025 (100 = przeciętny dzień)'
    ),
    vertical_spacing=0.13, horizontal_spacing=0.08
)

# Row 1: observed + trend
fig.add_trace(go.Scatter(x=monthly_total.index, y=monthly_total.values, mode='lines',
                         name='Obserwacje', line=dict(color='#185FA5', width=1.5)), row=1, col=1)
fig.add_trace(go.Scatter(x=trend.index, y=trend.values, mode='lines',
                         name='Trend (STL)', line=dict(color='#D85A30', width=2.5)), row=1, col=1)
fig.add_vrect(x0='2021-01-01', x1='2021-12-31', fillcolor='#cccccc', opacity=0.18,
              line_width=0, row=1, col=1,
              annotation_text='2021 — rozpędzanie zbioru (poza indeksem)',
              annotation_position='top left', annotation_font_size=10)

# Row 2 left: monthly seasonal index
colors_m = ['#185FA5' if v >= 100 else '#9bb8d4' for v in month_index.values]
fig.add_trace(go.Bar(x=MONTHS_PL, y=month_index.values, marker_color=colors_m,
                     showlegend=False), row=2, col=1)
fig.add_hline(y=100, line_dash='dash', line_color='#888', row=2, col=1)

# Row 2 right: day-of-week index
colors_d = ['#2E8B57' if v >= 100 else '#a9cdb8' for v in dow_index.values]
fig.add_trace(go.Bar(x=WEEKDAYS_PL, y=dow_index.values, marker_color=colors_d,
                     showlegend=False), row=2, col=2)
fig.add_hline(y=100, line_dash='dash', line_color='#888', row=2, col=2)

fig.update_layout(
    title=dict(text='Analiza sezonowości przetargów publicznych w Polsce (2021–2025)',
               font=dict(size=16)),
    height=850, width=1400, plot_bgcolor='white', paper_bgcolor='white',
    legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1)
)
fig.update_yaxes(title_text='Liczba przetargów', row=1, col=1, gridcolor='#f0f0f0')
fig.update_yaxes(title_text='Indeks', row=2, col=1, gridcolor='#f0f0f0')
fig.update_yaxes(title_text='Indeks', row=2, col=2, gridcolor='#f0f0f0')
fig.update_xaxes(gridcolor='#f0f0f0')

fig.write_html('output/seasonality.html')
fig.write_image('output/seasonality.png', scale=2)   # static image for report.md
print('\nZapisano: output/seasonality.html, output/seasonality.png, '
      'output/seasonality_monthly_index.csv')
fig.show()
