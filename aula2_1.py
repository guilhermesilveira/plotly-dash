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

# Supondo que 'dados' é o nosso DataFrame com a coluna 'age'
# Criar o histograma da distribuição das idades
figura_histograma = px.histogram(dados, x='age', title='Distribuição de Idade dos Pacientes')
# figura_histograma = px.histogram(dados.sample(n=10), x='age', title='Distribuição de Idade dos Pacientes')
# figura_histograma.show()


# Após a criação da visualização, é hora de adicioná-la ao layout. Neste ponto, ainda não estamos preocupados com o boxplot; queremos apenas garantir que o histograma apareça corretamente na nossa página.

from dash import Dash, html, dcc

# Inicializar a aplicação Dash, caso ainda não esteja inicializada
app = Dash(__name__)

# Definir o layout da aplicação para incluir apenas o histograma
app.layout = html.Div([
    html.H1('Análise deXXXX Doenças Cardíacas'),
    html.Div([
        html.H2('Distribuição de Idade dos Pacientes'),
        dcc.Graph(id='grafico-histograma-idade', figure=figura_histograma)
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)


# HOT RELOAD!!!! ENSINA HOT RELOAD!!!!
# primeiro de texto
# depois de dado?
# figura_histograma = px.histogram(dados.sample(n=10), x='age', title='Distribuição de Idade dos Pacientes')
