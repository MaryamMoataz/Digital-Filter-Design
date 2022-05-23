from re import template
import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import os


app = dash.Dash(external_stylesheets=[dbc.themes.SLATE])

# Set axes properties
fig.update_xaxes(range=[-1, 1],showgrid=False)
fig.update_yaxes(range=[-1, 1],showgrid=False)

# Add circles
fig.add_shape(type="circle",
    xref="x", yref="y",
    x0=-1, y0=-1, x1=1, y1=1,
    line_color="LightSeaGreen",
)


zplot = html.Div([html.MapEl([
        html.Area(target='', alt='otimizar', title='otimizar', href='https://www.google.com', coords='1,1,500,500', shape='circle'),
            ],name='map'),
            html.Img(src=app.get_asset_url('plot1.png') , useMap='#map')],style={'textAlign':'center'})


zplot_card = html.Div([
  dbc.Card([
    dbc.CardHeader("Z-Plot"),
    dbc.CardBody(zplot),
  ],)
])


phase_card = html.Div([
  dbc.Card([
    dbc.CardHeader("Phase"),
    dbc.CardBody(dcc.Graph(id ="plot_phase", figure=go.Figure(layout={'template':"plotly_dark"}))),
  ],className="opacity-50")
])


mag_card = html.Div([
  dbc.Card([
    dbc.Card([
    dbc.CardHeader("Phase",style={"background-color":"#ffffff"}),
    dbc.CardBody(dcc.Graph(id ="plot_mag", figure=go.Figure(layout={'template':"plotly_dark"}))),
  ],className="opacity-50")
])
])

operations_card = html.Div([
  dbc.Card([
    dbc.CardHeader("Operations"),
    dbc.CardBody(),
  ])
])


# app.layout = html.Div([
#   html.Div([
#     html.Div(
#       html.Div("hj",style={"float":"left", "width": "100px"})
#     ),
#     html.Div(
#       html.Div("hj",style={"float":"left", "width": "100px"})
#     )
#   ])
# ])

app.layout = html.Div([
  dbc.Row([
    dbc.Col([
      dbc.Row(mag_card),
      dbc.Row(phase_card)
    ],className="no-gutters padding-0",style= {
              "padding-right": "0 !important",
            
              }),
    dbc.Col([
      dbc.Row(operations_card),
      dbc.Row(zplot_card)
  ],className="no-gutters padding-0",style= {
              "padding-right": "0 !important",
              }),
],style= {
              "padding-right": "0 !important",
              })
        
])  
# app.layout = html.Div(children=[
#     html.Img(
# 		html.Map([
# 			html.Area(target='', alt='gerar', title='gerar', href='1', coords='427,136,319,89', shape='rect'),
# 			html.Area(target='', alt='otimizar', title='otimizar', href='2', coords='142,170,34,123', shape='rect'),
# 			html.Area(target='', alt='assegurar', title='assegurar', href='3', coords='283,170,173,120', shape='rect')],
# 			name='image-map'
# 		),
# 		src='plot1.png', 
# 		usemap='#image-map'
# 	),
#                         html.Div("",style= {
#                             "width": "100px",
#                             "height": "100px",
#                             "background": "#4bc475",
#                             "border": "1px solid #000"                    
#                                                     }),
#                         html.Div(dcc.Graph(figure=fig),style= {
#                                                       "color": "black",
#                                                       "background-color": "yellow",
#                                                       "border-style": "solid",                        
#                                                     }),
#                         html.Div(dcc.Graph(id ="plot_phase"),style= {
#                                                       "color": "black",
#                                                       "background-color": "yellow",
#                                                       "border-style": "solid",                        
#                                                     }),
#                         html.Div(dcc.Graph(id ="plot_mag"),style= {
#                                                       "color": "black",
#                                                       "background-color": "yellow",
#                                                       "border-style": "solid",                        
#                                                     })])
                                                    
app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter