# https://cloud.google.com/sdk/docs/install-sdk
# install
# criar projeto no console
# Dockerfile
# app.run_server(debug=False, host='0.0.0.0', port=8080)
# gcloud builds submit --tag gcr.io/aulaplotly1meu/heart-disease  --project=aulaplotly1meu
# gcloud run deploy heart-disease --image gcr.io/aulaplotly1meu/heart-disease --platform managed --project=aulaplotly1meu --allow-unauthenticated
# região 30
# gcloud app open-console
# https://console.cloud.google.com/run/detail/southamerica-east1/hd1/logs?project=aulaplotly1meu



# from pages62 import predict, charts
import pages62
from app62 import app





from dash import html, dcc
from dash.dependencies import Input, Output
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

import joblib
import pandas as pd




# Nesta seção, substitua ou adicione ao código existente da aplicação Dash para incluir o menu lateral
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Componente para controlar a URL do navegador
    dbc.Container([
    html.Nav([  # Container para o menu lateral
        dbc.Row([dbc.Col([dcc.Link('Home', href='/')])]),
        dbc.Row([dbc.Col([dcc.Link('Modelo', href='/modelo')])]),
        dbc.Row([dbc.Col([dcc.Link('Gráficos', href='/graficos')])])
    ], className="nav-menu"),  # Estilize sua coluna aqui ou use um arquivo CSS
    ]),
    html.Div(id='pagina-conteudo', className="content")  # Conteúdo que muda dependendo da página selecionada
])

# Este callback atualiza o conteúdo da página com base na URL
@app.callback(Output('pagina-conteudo', 'children'), [Input('url', 'pathname')])
def mostrar_pagina(pathname):
    if pathname == '/modelo':
        # Substituir este retorno pela página do modelo de doenças cardíacas quando criada
        return pages62.predict.layout
    elif pathname == '/graficos':
        return pages62.charts.layout
    else:
        return html.H1('Página Inicial')

print("O aplicativo está rodando com o menu lateral implementado.")

# Não se esqueça de iniciar seu servidor
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8080)

# Console logging para verificação
# ```

# Antes de executar o código acima, lembre-se de que qualquer estilo aplicado diretamente nos componentes pode ser movido para uma folha de estilo CSS externa para organização e reutilização do código. No exemplo, o estilo `{'columnCount': 1}` está sendo aplicado diretamente, mas poderia ser substituído por uma classe no arquivo CSS.