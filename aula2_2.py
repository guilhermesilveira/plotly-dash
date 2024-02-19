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



# Imprimir informação no console para acompanhar o processo
print('O histograma foi adicionado ao layout.')

# Execute a aplicação para ver o histograma em ação. Após confirmar que está funcionando como o esperado, é hora de dar o próximo passo e adicionar o boxplot ao nosso layout.

# Para criar o boxplot, precisamos de outra coluna em nosso DataFrame que indique se o paciente possui ou não doença cardíaca. Assim como no exemplo real que demos com os nomes de João, Maria e Ana, iremos agora concretizar essa lógica no nosso código:

# Verificando se a coluna 'doenca' existe e criando-a se necessário
dados['doenca'] = dados['doenca'].apply(lambda x: 'Com Doença Cardíaca' if x == 1 else 'Sem Doença Cardíaca')

# Agora, vamos criar o gráfico boxplot
figura_boxplot = px.box(dados, x='doenca', y='age', title='Idade por Presença de Doença Cardíaca')
# figura_boxplot = px.box(dados, x='doenca', y='age', color='doenca',
                        # title='Idade por Presença de Doença Cardíaca',
                        # color_discrete_map={'Sem Doença Cardíaca': 'blue', 'Com Doença Cardíaca': 'red'}
                        # )
                        # figura_boxplot.update_traces(marker_color=['blue', 'red'])


# Com o boxplot pronto, queremos adicioná-lo ao nosso layout da mesma forma que fizemos com o histograma, garantindo que ambos os gráficos estejam disponíveis para visualização na aplicação:

# No layout existente, adicionar o novo boxplot
app.layout.children.append(
    html.Div([
        html.H2('Idade por Presença de Doença Cardíaca'),
        dcc.Graph(id='grafico-boxplot-doenca', figure=figura_boxplot)
    ])
)

# USE GITHUB COPILOT!!!!!!!!!!!!!
# change the color of the second boxplot to red
# figura_boxplot.update_traces(marker_color='red')

# USE CHATGPT!!!!!
# https://chat.openai.com/share/21a1088c-bd01-4e1e-9359-8e2c23923175
# figura_boxplot = px.box(dados, x='doenca', y='age', color='doenca',
                        # title='Idade por Presença de Doença Cardíaca',
                        # color_discrete_map={'Sem Doença Cardíaca': 'blue', 'Com Doença Cardíaca': 'red'}
                        # )
                        # figura_boxplot.update_traces(marker_color=['blue', 'red'])



# Log para confirmar que o boxplot foi adicionado
print('O boxplot foi adicionado ao layout.')

# E aí está! Execute a aplicação novamente e certifique-se de que ambos os gráficos - o histograma das idades e o boxplot da idade por presença de doença cardíaca - estão aparecendo na página corretamente.

# Em termos menos concretos, você aprendeu como adicionar visualizações de dados interativas a uma aplicação web usando Dash com o auxílio da biblioteca Plotly Express. Agora, você possui um recurso visual poderoso que permite aos usuários explorar e interpretar os dados de maneira dinâmica e informativa.


if __name__ == '__main__':
    app.run_server(debug=True)
