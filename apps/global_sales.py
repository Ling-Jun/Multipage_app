import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
# ../Multipage_App/apps
DATA_PATH = PATH.joinpath("../datasets").resolve()
# ../Multipage_App/datasets
# The path. resolve() method resolves a sequence of paths or path segments into an absolute path.
# path.join('/a', '/b') // Outputs '/a/b', while path.resolve('/a', '/b') // Outputs '/b' 


# owner: shivp Kaggle. Source: https://data.mendeley.com/datasets
# dataset was modified. Original data: https://www.kaggle.com/shivkp/customer-behaviour
dfg = pd.read_csv(DATA_PATH.joinpath("opsales.csv"))

layout = html.Div([
    html.H1('General Product Sales', style={"textAlign": "center"}),

    html.Div([
        html.Div([
            html.Pre(children="Payment type", style={"fontSize":"150%"}),
            dcc.Dropdown(
                id='pymnt-dropdown', value='DEBIT', clearable=False,
                persistence=True, persistence_type='session',
                # persistence, Used to allow user interactions in this component to be persisted when the component - or the page - is refreshed
                # For example, perhaps you have dropdowns for country and city, and you know that your users want to see the same country 
                # pre-filled as the last time they used your app - you can just set persistence=True on the country dropdown. 
                # But for the city they would like to see the same one as the last time they chose that country - 
                # just set persistence=country_name (where country_name is the value of the chosen country) on the city dropdown and 
                # we'll save one preferred city for each country.
                # 
                # persistence_type = 'session' uses window.sessionStorage. Like 'local' the data is kept when you reload the page, 
                # but cleared when you close the browser or open the app in a new browser tab.
                options=[{'label': x, 'value': x} for x in sorted(dfg["Type"].unique())]
            )
        ], className='six columns'),

        html.Div([
            html.Pre(children="Country of destination", style={"fontSize": "150%"}),
            dcc.Dropdown(
                id='country-dropdown', value='India', clearable=False,
                persistence=True, persistence_type='local',
                options=[{'label': x, 'value': x} for x in sorted(dfg["Order Country"].unique())]
            )
            ], className='six columns'),
    ], className='row'),

    dcc.Graph(id='my-map', figure={}),
])


@app.callback(
    Output(component_id='my-map', component_property='figure'),
    [Input(component_id='pymnt-dropdown', component_property='value'),
     Input(component_id='country-dropdown', component_property='value')]
)
def display_value(pymnt_chosen, country_chosen):
    dfg_fltrd = dfg[(dfg['Order Country'] == country_chosen) &
                    (dfg["Type"] == pymnt_chosen)]
    dfg_fltrd = dfg_fltrd.groupby(["Customer State"])[['Sales']].sum()
    dfg_fltrd.reset_index(inplace=True)
    # px.choropleth() 
    fig = px.choropleth(dfg_fltrd, locations="Customer State",
                        locationmode="USA-states", color="Sales",
                        scope="usa")
    return fig

