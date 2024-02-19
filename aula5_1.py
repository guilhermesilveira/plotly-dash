# # Item #6.1
# Nome da Tarefa: Implementar um menu lateral com dois links para duas páginas, a primeira é o modelo, a segunda vazia
# Problema: Necessidade de melhorar a estrutura de navegação do aplicativo Dash
# Solução: Criação de um layout com navegação lateral que contém links para diferentes páginas
# Teoria: Navegação entre páginas em Dash

# Tarefa: Implementar no aplicativo Dash um menu lateral que permita ao usuário alternar entre uma página que apresenta o modelo de previsão de doenças cardíacas e outra página que será desenvolvida posteriormente.

# Problema concreto: O projeto precisa de uma forma organizada e intuitiva para que os usuários possam navegar entre as diferentes funcionalidades do aplicativo. Adicionando um menu lateral, você permitirá que os usuários alternem entre a visualização do modelo de previsão e outras partes do aplicativo que podem ser implementadas no futuro.

# File "app.py"
# # ```python
# Adicione estas importações no topo do seu arquivo app.py, próximo às outras importações
from dash import html, dcc
from dash.dependencies import Input, Output
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import joblib
import pandas as pd

app = Dash(__name__)

# Nesta seção, substitua ou adicione ao código existente da aplicação Dash para incluir o menu lateral
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),  # Componente para controlar a URL do navegador
    html.Nav([  # Container para o menu lateral
        dcc.Link('Modelo de Doenças Cardíacas', href='/modelo-cardiaco'),
        html.Br(),
        dcc.Link('Página Vazia', href='/pagina-vazia'),
    ], className="mynav"),  # Estilize sua coluna aqui ou use um arquivo CSS
    html.Div(id='pagina-conteudo')  # Conteúdo que muda dependendo da página selecionada
])

# Este callback atualiza o conteúdo da página com base na URL
@app.callback(Output('pagina-conteudo', 'children'), [Input('url', 'pathname')])
def mostrar_pagina(pathname):
    if pathname == '/modelo-cardiaco':
        # Substituir este retorno pela página do modelo de doenças cardíacas quando criada
        return html.H1('Página do Modelo de Doenças Cardíacas')
    elif pathname == '/pagina-vazia':
        return html.H1('Página Vazia')
    else:
        return html.H1('Página Inicial')

# Não se esqueça de iniciar seu servidor
if __name__ == '__main__':
    app.run_server(debug=True)

# Console logging para verificação
print("O aplicativo está rodando com o menu lateral implementado.")
# ```

# Antes de executar o código acima, lembre-se de que qualquer estilo aplicado diretamente nos componentes pode ser movido para uma folha de estilo CSS externa para organização e reutilização do código. No exemplo, o estilo `{'columnCount': 1}` está sendo aplicado diretamente, mas poderia ser substituído por uma classe no arquivo CSS.