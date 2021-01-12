import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import vgames, global_sales


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    # dcc.Location() represents the location bar in your web browser through the pathname property.  
    html.Div([
        dcc.Link('Video Games|', href='/apps/vgames'),
        # The Link element updates the pathname of the browser without refreshing the page.
        dcc.Link('Other Products', href='/apps/global_sales'),
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/vgames':
        # layout in vgames.py file
        return vgames.layout
    if pathname == '/apps/global_sales':
        return global_sales.layout
    else:
        return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)