from dash import html, dcc
import plotly.graph_objs as go
from dash import html, dcc
from dash.dependencies import Input, Output
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

import plotly.express as px
from ucimlrepo import fetch_ucirepo

# https://github.com/uci-ml-repo/ucimlrepo/issues/6

import ssl

# Ignore ssl certificate verification
ssl._create_default_https_context = ssl._create_unverified_context


# Aqui estamos buscando o dataset específico de doenças cardíacas da UCI
heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features
dados['doenca'] = 1 * (heart_disease.data.targets > 0)
# print(dados.head())




# Você está diante do desafio de enriquecer a sua aplicação web com visualizações que permitam uma análise mais aprofundada do conjunto de dados sobre doenças cardíacas. Já temos um histograma que retrata a distribuição das idades dos pacientes, mas agora queremos agregar ainda mais valor ao nosso dashboard com a inclusão de um boxplot.

# Vamos começar adicionando o histograma no layout da nossa aplicação Dash. Imagine que temos dados de pacientes, e queremos ver como as idades estão distribuídas. Utilizando a biblioteca Plotly Express, criaremos o gráfico da seguinte maneira:

import plotly.express as px

figura_histograma = px.histogram(dados, x='age', title='Distribuição de Idade dos Pacientes')

# Verificando se a coluna 'doenca' existe e criando-a se necessário
dados['doenca'] = dados['doenca'].apply(lambda x: 'Com Doença Cardíaca' if x == 1 else 'Sem Doença Cardíaca')

# Agora, vamos criar o gráfico boxplot
# figura_boxplot = px.box(dados, x='doenca', y='age', title='Idade por Presença de Doença Cardíaca')
figura_boxplot = px.box(dados, x='doenca', y='age', color='doenca',
                        title='Idade por Presença de Doença Cardíaca',
                        )

layout = dbc.Container([
    html.H1('Análise de Doenças Cardíacas', className='text-center mb-5'),
    dcc.Dropdown(
        id='cp-dropdown',
        options=[
            {'label': 'Tipo 1', 'value': 1},
            {'label': 'Tipo 2', 'value': 2},
            {'label': 'Tipo 3', 'value': 3},
            {'label': 'Tipo 4', 'value': 4}
        ],
    ),
    html.Div(id='tosco'),
    dbc.Row([
        dbc.Col([
            html.H2('Distribuição de Idade dos Pacientes', className='text-center'),
            dcc.Graph(id='grafico-histograma-idade', figure=figura_histograma)
        ], md=9),
        dbc.Col([
            html.H2('Idade por Presença de Doença Cardíaca', className='text-center'),
            dcc.Graph(id='grafico-boxplot-doenca', figure=figura_boxplot)
        ], md=3),
    ])
], fluid=True)

    # print(f"Definindo callback")
    # @app.callback(
    #     Output('grafico-histograma-idade', 'figure'),
    #     [Input('cp-dropdown', 'value')]
    # )


def setup_layout(app):
    # @app.callback(
    #         Output('tosco', 'children'),
    #         Input('cp-dropdown', 'value')
    #     )
    @app.callback(
        Output('grafico-histograma-idade', 'figure'),
        [Input('cp-dropdown', 'value')]
    )
    def update_graph(selected_cp):
        # print("ha")
        # return html.H1('Análise de Doenças Cardíacas', className='text-center mb-5')

        filtered_df = df[df['cp'] == selected_cp]
        fig = px.histogram(dados, x='age', title='Distribuição de Idade dos Pacientes')
        # fig = px.histogram(filtered_df, x='age', title="Distribuição de Idade por Valor de CP")
        print(f"Figura atualizada para cp = {selected_cp}")
        return fig
