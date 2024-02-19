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

# z is everything but doenca
X = dados.drop(['doenca'], axis=1)
y = dados['doenca']


from sklearn.model_selection import train_test_split
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2, stratify=y, random_state=432)

import xgboost as xgb

xg_cl = xgb.XGBClassifier(objective='binary:logistic')
xg_cl.fit(X_treino, y_treino)
preds = xg_cl.predict(X_teste)

from sklearn.metrics import accuracy_score


acuracia = accuracy_score(y_teste, preds)
print(f'Acuracia: {acuracia:.2f}')

from sklearn.metrics import classification_report


report = classification_report(y_teste, preds)
print(report)

# https://github.com/vqrca/classificacao_xgboost/blob/main/Aulas/Aula_5.ipynb
# por educacao seria o ultimo modelo, mas nao eh nosso foco discutir treino de modelo aqui

import joblib

joblib.dump(xg_cl, 'modelo_xgboost.pkl')




# ISSO AQUI EH NA AULA 4.1
medianas = X.median()

# Salvando as medianas em um arquivo pickle
joblib.dump(medianas, 'medianas.pkl')

print("Mediana dos campos salva com sucesso.")
