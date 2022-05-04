import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as xp


# this options list will be needed in the dcc.Dropdown componenet setting 
options=[{'label':region,'value':region} for region in ['east','north','west','south']]

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

sales=pd.read_csv('response.csv')
# create sales dataframe by regions east west north and south
salesE=sales[sales['region']=='east'][['date','Sales']]
salesN=sales[sales['region']=='north'][['date','Sales']]
salesW=sales[sales['region']=='west'][['date','Sales']]
salesS=sales[sales['region']=='south'][['date','Sales']]


app=dash.Dash()
app.layout = html.Div([
    html.H1(children='Sales Evolution by Date ',style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    
    
    dcc.Dropdown(
    id='select_region',    
    options=options,
    value='east' #default value
    ),  
    html.Div(id='displaySales',style={
            'textAlign': 'center',
            'color':'red'}),  
    dcc.Graph(id='chart',figure={})
])
@app.callback(
    [Output(component_id='displaySales', component_property='children'),
    Output(component_id='chart', component_property='figure')],
    [Input(component_id='select_region', component_property='value')]
    
)
def update(input_value):
    d={'east':salesE,'west':salesW,'north':salesN,'south':salesS}
    
    df=d[input_value]
    # plotly 
    fig = xp.line(df, x='date', y='Sales')
    fig.add_annotation(x='2021-1-15',y=2195.0, text="15th of January, 2021")
    fig.update_layout(hovermode="x")
    return f'Sales in {input_value.capitalize()} Region',fig

if __name__ == '__main__':
    app.run_server(debug=True)