import plotly.graph_objects as go

valoresAY = [3273, 2970, 3145, 3148, 3469, 3802, 5226, 5590, 6798]
valoresBY = [81, 97, 117, 140, 168, 202, 413, 812, 884]
valoresCY = [10, 12, 15, 20, 32, 186, 411, 519, 851]
valoresDY = [129, 129, 132, 99, 140, 489, 1897, 1612, 2123]
valoresEY = [6559, 6247, 6341, 6689, 6636, 5342, 3113, 2651, 3136]
valoresFY = [1349, 1232, 1241, 1299, 1296, 902, 249, 125, 210]
valoresX = [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]

fig = go.Figure()
fig.add_trace(go.Scatter(x=valoresX, y=valoresAY, mode='lines+markers', name='BIOBOLSAS'))
fig.add_trace(go.Scatter(x=valoresX, y=valoresBY, mode='lines+markers', name='BOLSAS PAPEL'))
fig.add_trace(go.Scatter(x=valoresX, y=valoresCY, mode='lines+markers', name='BOLSAS PEAD'))
fig.add_trace(go.Scatter(x=valoresX, y=valoresDY, mode='lines+markers', name='BOLSAS PEBD'))
fig.add_trace(go.Scatter(x=valoresX, y=valoresEY, mode='lines+markers', name='BOLSAS PP'))
fig.add_trace(go.Scatter(x=valoresX, y=valoresFY, mode='lines+markers', name='OTRAS BOLSAS PLÁSTICAS'))

fig.update_layout(title='Mi gráfico', xaxis_title='Año', yaxis_title='Valor', legend_title='Leyenda')

fig.write_html('grafico.html')