import pages62
from app62 import app



# criar projeto no console
# Dockerfile
# app.run_server(debug=False, host='0.0.0.0', port=8080)
# criar o build no console


# https://cloud.google.com/sdk/docs/install-sdk
# install
# gcloud builds submit --tag gcr.io/aulaplotly1meu/heart-disease  --project=aulaplotly1meu
# gcloud run deploy heart-disease --image gcr.io/aulaplotly1meu/heart-disease --platform managed --project=aulaplotly1meu --allow-unauthenticated
# região 30
# gcloud app open-console
# https://console.cloud.google.com/run/detail/southamerica-east1/hd1/logs?project=aulaplotly1meu


from dash import html, dcc
from dash.dependencies import Input, Output
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

import joblib
import pandas as pd



navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Modelo", href="/modelo")),
        dbc.NavItem(dbc.NavLink("Gráficos", href="/graficos")),
    ],
    brand="Nosso projeto 2",
    brand_href="/",
    color="primary",
    dark=True,
)

# Nesta seção, substitua ou adicione ao código existente da aplicação Dash para incluir o menu lateral
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Componente para controlar a URL do navegador
    navbar,
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
        return html.H1('Bem vindo ao nosso projeto')

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8080)
    # app.run_server(debug=True)
