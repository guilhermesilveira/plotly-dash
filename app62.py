from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# TODO MUDADO
# app = Dash(__name__, external_stylesheets=['assets/main.css'])
app = Dash(__name__, external_stylesheets=['assets/main.css',dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True)
