# Item #5.2
# Nome da Tarefa: Criar o formulário completo para cada campo após carregar o modelo pickle
# Problema: Incorporar previsões de ML no aplicativo web Dash
# Solução: Usar componentes do Dash Core para criar um formulário com entrada de dados do usuário e exibir os resultados da predição
# Teoria: Componentes do Core Dash, integrando ML com Dash

# Tarefa à Mão: Agora que você criou um formulário simples para a entrada da idade do usuário, você vai adaptar o layout do aplicativo Dash para incluir campos para todos os parâmetros que o modelo de machine learning requer para fazer uma predição.

import joblib

modelo = joblib.load('modelo_xgboost.pkl')


# Problema Concreto: Você precisa construir um formulário completo com campos para todas as variáveis necessárias pelo modelo de predição de doenças cardíacas. O usuário deverá ser capaz de inserir seus dados e receber uma previsão instantânea sobre o risco de doença cardíaca.

# File "app.py"
# ```python
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import joblib
import pandas as pd

# Carrega o modelo treinado
modelo = joblib.load('modelo_xgboost.pkl')

app = Dash(__name__)

# Definição do layout do aplicativo Dash incluindo todos os campos necessários para a entrada de dados
app.layout = html.Div([
    html.H1('Previsão de Doença Cardíaca'),
    html.Div([
        # label
        html.Label('Idade'),
        dcc.Input(id='idade', type='number', placeholder='Idade'),
        html.Br(),
        # label
        html.Label('Sexo (1 para masculino, 0 para feminino)'),
        # combo
        dcc.Dropdown(
            id='sexo',
            options=[
                {'label': 'Masculino', 'value': 1},
                {'label': 'Feminino', 'value': 0}
            ],
        ),
        html.Br(),
        # label
        html.Label('Tipo de Dor no Peito (1 a 4)'),
        # combo
        dcc.Dropdown(
            id='cp',
            options=[
                {'label': 'Tipo 1', 'value': 1},
                {'label': 'Tipo 2', 'value': 2},
                {'label': 'Tipo 3', 'value': 3},
                {'label': 'Tipo 4', 'value': 4}
            ],
        ),
        # dcc.Input(id='cp', type='number', placeholder='Tipo de Dor no Peito (1 a 4)'),
        # label
        html.Label('Pressão Sanguínea em Repouso'),
        dcc.Input(id='trestbps', type='number', placeholder='Pressão Sanguínea em Repouso'),
        # label
        html.Label('Colesterol sérico'),
        dcc.Input(id='chol', type='number', placeholder='Colesterol sérico'),
        # label
        html.Label('Glicose em Jejum > 120 mg/dl (1 para verdadeiro)'),
        # combo
        dcc.Dropdown(
            id='fbs',
            options=[
                {'label': 'Não', 'value': 0},
                {'label': 'Sim', 'value': 1}
            ],
        ),
        # dcc.Input(id='fbs', type='number', placeholder='Glicose em Jejum > 120 mg/dl (1 para verdadeiro)'),
        # label
        html.Label('Resultados Eletrocardiográficos em Repouso (0 a 2)'),
        # select options
        dcc.Dropdown(
            id='restecg',
            options=[
                {'label': 'Normal', 'value': 0},
                {'label': 'Anormalidade de ST-T', 'value': 1},
                {'label': 'Hipertrofia Ventricular Esquerda', 'value': 2}
            ],
        ),
        # dcc.Input(id='restecg', type='number', placeholder='Resultados Eletrocardiográficos em Repouso (0 a 2)'),
        # label
        html.Label('Frequência Cardíaca Máxima'),
        dcc.Input(id='thalach', type='number', placeholder='Frequência Cardíaca Máxima'),
        # label
        html.Label('Angina Induzida por Exercício (1 para sim)'),
        # dropbox
        dcc.Dropdown(
            id='exang',
            options=[
                {'label': 'Não', 'value': 0},
                {'label': 'Sim', 'value': 1}
            ],
        ),

        # dcc.Input(id='exang', type='number', placeholder='Angina Induzida por Exercício (1 para sim)'),
        # label
        html.Label('Depressão de ST Induzida por Exercício'),
        dcc.Input(id='oldpeak', type='number', placeholder='Depressão de ST Induzida por Exercício'),
        # label
        html.Label('Inclinação do Segmento ST no Pico do Exercício (1 a 3)'),
        # dropdown
        dcc.Dropdown(
            id='slope',
            options=[
                {'label': 'Inclinação para Cima', 'value': 1},
                {'label': 'Plano', 'value': 2},
                {'label': 'Inclinação para Baixo', 'value': 3}
            ],
        ),
        # dcc.Input(id='slope', type='number', placeholder='Inclinação do Segmento ST no Pico do Exercício (1 a 3)'),
        # label
        html.Label('Número de Vasos Principais Coloridos por Fluoroscopia (0 a 3)'),
        dcc.Input(id='ca', type='number', placeholder='Número de Vasos Principais Coloridos por Fluoroscopia (0 a 3)'),
        # label
        html.Label('Cintilografia do miocárdio com tálio (3 para normal, 6 para defeito fixo, 7 para defeito reversível)'),
        # combo com padrao o valor vazio
        dcc.Dropdown(
            id='thal',
            options=[
                {'label': 'Normal', 'value': 3},
                {'label': 'Defeito Fixo', 'value': 6},
                {'label': 'Defeito Reversível', 'value': 7}
            ]
        ),
        # dcc.Input(id='thal', type='number', placeholder='Cintilografia do miocárdio (3 para normal, 6 para defeito fixo, 7 para defeito reversível)'),

        html.Button('Prever', id='prever', n_clicks=0),
    ]),
    html.Div(id='resultado')
])

# problema de valor default: a pessoa esquece de alterar!!!!



# AULA 4.1!!!!

import pandas as pd
import joblib


# Supondo que o modelo já foi carregado anteriormente
# modelo = joblib.load('modelo_xgboost.pkl')

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
        
        # Faz a predição com os dados do usuário
        predicao = modelo.predict(entradas_usuario)[0]
        
        return f'O modelo previu que o paciente {"tem" if predicao else "não tem"} doença cardíaca.'
    return 'Informe seus dados e clique em prever para receber a previsão.'





if __name__ == '__main__':
    app.run_server(debug=True)
# ```

# Antes de executar esse código, lembre-se de ter o modelo 'modelo_xgboost.pkl' no mesmo diretório do arquivo 'app.py'. Este código espera receber os dados especificados e chamará o modelo treinado para prever a presença ou ausência de doença cardíaca baseado nesses dados.