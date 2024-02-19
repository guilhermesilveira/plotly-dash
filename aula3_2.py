## #5.1 - Incorporando Predições de ML no Aplicativo Web Dash
### #5.1 - Criar formulário com Dash Core Components apenas para o campo idade


# Vamos imaginar que você precisa criar um formulário em um aplicativo web usando a biblioteca Dash, que servirá para inserir a idade de um usuário. Após submeter essa idade usando um botão, você quer que ela seja exibida na tela. Por exemplo, se a usuária Joana inserir "29" e apertar o botão "Submeter", o aplicativo deverá mostrar "A idade inserida é: 29". 

# Primeiro, é necessário iniciar o seu aplicativo Dash. Para isso, você precisa criar uma instância do Dash no seu código. Isso é como abrir o seu programa para começar a trabalhar nele.

# ```python
import dash
from dash import html, dcc

# Crie uma instância do aplicativo Dash
app = dash.Dash(__name__)
# ```

# Agora que você tem o aplicativo inicializado, o próximo passo é definir o layout. O layout vai determinar o que será mostrado na sua aplicação web. Você vai começar adicionando um campo de entrada de texto para a idade e um botão para submeter essa idade.

# ```python
# Defina o layout do aplicativo
app.layout = html.Div([
    dcc.Input(id='input-idade', type='number', placeholder='Insira sua idade'),
    html.Button('Submeter', id='botao-submeter', n_clicks=0),
])
# ```

# Quando você adiciona um `dcc.Input` com `type='number'`, está dizendo ao Dash que espera que os usuários digitem números nesse campo, como a idade deles. Também estamos dando ao botão um `id` e definindo `n_clicks` para zero, porque ele ainda não foi clicado.

# Agora precisamos de uma maneira de mostrar a idade na tela depois que o botão for pressionado. Vamos adicionar um elemento `html.Div` ao layout onde a idade será exibida após o botão ser clicado.

# ```python
app.layout.children.append(html.Div(id='container-idade'))
# ```

# A seguir, você criará a função de callback. Callbacks são funções que atualizam uma parte do seu aplicativo em resposta a alguma interação do usuário. Você quer que, após o botão ser clicado, a idade digitada seja exibida.

# ```python
from dash.dependencies import Input, Output, State

# Define a função de callback para atualizar o componente de exibição de idade
@app.callback(
    Output('container-idade', 'children'),
    [Input('botao-submeter', 'n_clicks')],
    [State('input-idade', 'value')]
)
def atualizar_saida(n_clicks, valor_idade):
    if n_clicks > 0:
        return f'A idade inserida é: {valor_idade}'
    else:
        return 'Insira sua idade e clique em Submeter'
# ```

# Quando você define `Output('container-idade', 'children')`, está especificando que quer atualizar os "filhos" do componente com ID `container-idade`. E com `Input('botao-submeter', 'n_clicks')` e `State('input-idade', 'value')`, você está dizendo ao Dash para usar o número de cliques no botão e o valor no campo idade como entradas para a função de callback `atualizar_saida`. 
# 
# Para testar a funcionalidade dessa parte do código, você pode incluir uma mensagem de log:

# ```python
print("Callback criado com sucesso e esperando a interação do usuário.")
# ```

# Por fim, para iniciar o servidor e ver sua aplicação funcionando, use:

# Agora, de maneira não concreta: o que fizemos foi criar um formulário utilizando os componentes do Dash que permite a interação do usuário. A aplicação web agora tem a capacidade de receber input de idade, que é processada por uma função de callback, e a exibição dessa informação é atualizada dinamicamente na tela. Usamos os conceitos básicos de uma interface de usuário e programação reativa para construir a funcionalidade desejada.

if __name__ == '__main__':
    app.run_server(debug=True)
