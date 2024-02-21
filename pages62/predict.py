from dash import html, dcc
import plotly.graph_objs as go
from app62 import app

from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import joblib
import pandas as pd
import dash_bootstrap_components as dbc
import dash

#hd1

# Carrega o modelo treinado
modelo = joblib.load('modelo_xgboost.pkl')

# Definição do layout do aplicativo Dash
layout = dbc.Container([
    html.H1('Previsão de Doença Cardíaca',className='text-center mt-5'),
    html.P('Informe os dados do paciente e clique em prever para receber a previsão.', className='text-center mb-5'),
    dbc.Row([
        dbc.Col([
            dbc.CardGroup([
                dbc.Label('Idade'),
                dbc.Input(id='idade', type='number', placeholder='Digite a idade'),
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
                dbc.Input(id='trestbps', type='number', placeholder='Digite a pressão sanguínea em repouso'),
            ],className='mb-3'),
            dbc.CardGroup([
                dbc.Label('Colesterol sérico'),
                dbc.Input(id='chol', type='number', placeholder='Digite o colesterol sérico'),
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
                dbc.Input(id='thalach', type='number', placeholder='Digite a frequência cardíaca máxima'),
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
                dbc.Input(id='oldpeak', type='number', placeholder='Digite a depressão de ST induzida por exercício'),
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
                dbc.Label('Número de Vasos Principais Coloridos por Fluoroscopia'),
                dbc.Select(
                    id='ca',
                    options=[
                        {'label':'0', 'value':0},
                        {'label':'1', 'value':1},
                        {'label':'2', 'value':2},
                        {'label':'3', 'value':3},
                    ],
                ),
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

# Carrega as medianas dos campos
medianas = joblib.load('medianas.pkl')

@app.callback(
    Output('resultado', 'children'),
    [Input('prever', 'n_clicks')],
    [State('idade', 'value'),
     State('sexo', 'value'),
     State('cp', 'value'),
     State('trestbps', 'value'),
     State('chol', 'value'),
     State('fbs', 'value'),
     State('restecg', 'value'),
     State('thalach', 'value'),
     State('exang', 'value'),
     State('oldpeak', 'value'),
     State('slope', 'value'),
     State('ca', 'value'),
     State('thal', 'value')]
)


def prever_doenca_cardiaca(n_clicks, idade, sexo, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    if n_clicks > 0:
        # Cria um DataFrame com as entradas do usuário
        entradas_usuario = pd.DataFrame(
            data=[[idade, sexo, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
            columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
        )

        # Preenche os valores vazios com as medianas
        entradas_usuario.fillna(medianas, inplace=True)

        # Lista de colunas para converter para int, exceto 'oldpeak'
        colunas_para_int = ['sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'slope', 'ca', 'thal']

        # Convertendo 'oldpeak' para float separadamente
        entradas_usuario['oldpeak'] = entradas_usuario['oldpeak'].astype(float)

        # Loop para converter as demais colunas para int
        for coluna in colunas_para_int:
            entradas_usuario[coluna] = entradas_usuario[coluna].astype(int)
        
        # Faz a predição com os dados do usuário
        predicao = modelo.predict(entradas_usuario)[0]
        
            # Cria o alerta com a mensagem
        mensagem = f'O modelo previu que o paciente {"tem" if predicao else "não tem"} doença cardíaca.'
        cor_do_alerta = "danger" if predicao else "light"  # Define a cor com base na predição

        alerta = dbc.Alert(
        mensagem,
        color=cor_do_alerta,  # Usa a cor definida com base na predição
        className="d-flex justify-content-center",  # Centraliza o texto no alerta
        )
        return alerta
        #return f'O modelo previu que o paciente {"tem" if predicao else "não tem"} doença cardíaca.'
    #return 'Informe seus dados e clique em prever para receber a previsão.'

