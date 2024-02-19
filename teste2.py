from dash import Dash, html, dcc
import joblib
import pandas as pd
import dash_bootstrap_components as dbc
import dash

# Carrega o modelo treinado
modelo = joblib.load('modelo_xgboost.pkl')

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

# Definição do layout do aplicativo Dash
app.layout = dbc.Container([
    html.H1('Previsão de Doença Cardíaca',className='text-center mt-5'),
    html.P('Informe os dados do paciente e clique em prever para receber a previsão.', className='text-center mb-5'),
    dbc.Row([
        dbc.Col([
            dbc.CardGroup([
                dbc.Label('Idade'),
                dbc.Input(id='idade', type='number', placeholder='Idade'),
            ],className='mb-3'),
            dbc.CardGroup([
                dbc.Label('Sexo biológico'),
                dbc.Select(
                    id='sexo',
                    options=[
                        {'label': 'Masculino', 'value': 1},
                        {'label': 'Feminino', 'value': 0},
                    ],
                ),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('Tipo de Dor no Peito'),
                dbc.Select(
                    id='cp',
                    options=[
                        {'label': 'Angina típica', 'value': 1},
                        {'label': 'Angina atípica', 'value': 2},
                        {'label': 'Não angina', 'value': 3},
                        {'label': 'Angina assintomática', 'value': 4},
                    ],
                ),
            ],className='mb-3'),
            dbc.CardGroup([
                dbc.Label('Pressão Sanguínea em Repouso'),
                dbc.Input(id='trestbps', type='number', placeholder='Pressão Sanguínea em Repouso'),
            ],className='mb-3'),
            dbc.CardGroup([
                dbc.Label('Colesterol sérico'),
                dbc.Input(id='chol', type='number', placeholder='Colesterol sérico'),
            ],className='mb-3'),
            dbc.CardGroup([
                dbc.Label('Glicose em Jejum > 120 mg/dl'),
                dbc.Select(
                    id='fbs',
                    options=[
                        {'label': 'Não', 'value': 0},
                        {'label': 'Sim', 'value': 1},
                    ],
                ),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('Resultados Eletrocardiográficos em Repouso'),
                dbc.Select(
                    id='restecg',
                    options=[
                        {'label': 'Normal', 'value': 0},
                        {'label': 'Anormalidade de ST-T', 'value': 1},
                        {'label': 'Hipertrofia Ventricular Esquerda', 'value': 2},
                    ],
                ),
            ], className='mb-3'),
        ], md=5),
        dbc.Col([
            dbc.CardGroup([
                dbc.Label('Frequência Cardíaca Máxima'),
                dbc.Input(id='thalach', type='number', placeholder='Frequência Cardíaca Máxima'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('Angina Induzida por Exercício'),
                dbc.Select(
                    id='exang',
                    options=[
                        {'label': 'Não', 'value': 0},
                        {'label': 'Sim', 'value': 1},
                    ],
                ),
            ],className='mb-3'),
            dbc.CardGroup([
                dbc.Label('Depressão de ST Induzida por Exercício'),
                dbc.Input(id='oldpeak', type='number', placeholder='Depressão de ST Induzida por Exercício'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('Inclinação do Segmento ST no Pico do Exercício'),
                dbc.Select(
                    id='slope',
                    options=[
                        {'label': 'Inclinação para Cima', 'value': 1},
                        {'label': 'Plano', 'value': 2},
                        {'label': 'Inclinação para Baixo', 'value': 3},
                    ],
                ),
            ],className='mb-3'),
            dbc.CardGroup([
                dbc.Label('Número de Vasos Principais Coloridos por Fluoroscopia (0 a 3)'),
                dbc.Input(id='ca', type='number', placeholder='Número de Vasos Principais Coloridos por Fluoroscopia (0 a 3)'),
            ], className='mb-3'),
            dbc.CardGroup([
                dbc.Label('Cintilografia do miocárdio com tálio'),
                dbc.Select(
                    id='thal',
                    options=[
                        {'label': 'Normal', 'value': 3},
                        {'label': 'Defeito Fixo', 'value': 6},
                        {'label': 'Defeito Reversível', 'value': 7},
                    ],
                ),
            ]),
            dbc.Button('Prever', id='prever', color='success', n_clicks=0, className='mt-5 mb-5'),
        ], md=6),
    ]),
    html.Div(id='resultado'),
    html.Div(className='mb-5'),
], fluid=True, className='px-5')

# Callbacks e funções do aplicativo ficam inalteradas

if __name__ == '__main__':
    app.run_server(debug=True)
