import plotly
import plotly.figure_factory as ff
# import sys
# from sql_queries import Expired_Patron

plotly.offline.init_notebook_mode(connected=True)

# print(Expired_Patron)
# argvlist = sys.argv

def expired_patrons(data):
    table1 = ff.create_table(data)
    plotly.offline.iplot(table1)

def ill_lending_map(ill):
    scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
                [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]
    data = [ dict(
            type='choropleth',
            colorscale = scl,
            autocolorscale = False,
            locations = ill[0],
            z = ill[1],
            locationmode = 'USA-states',
            marker = dict(
                line = dict (
                    color = 'rgb(255,255,255)',
                    width = 2
                ) ),
            colorbar = dict(
                title = "Lending Count")
            ) ]

    layout = dict(
            title = 'Interlibary Loan Lending by State<br>(Hover for breakdown)',
            geo = dict(
                scope='usa',
                projection=dict( type='albers usa' ),
                showlakes = True,
                lakecolor = 'rgb(255, 255, 255)'),
                )
        
    fig = dict( data=data, layout=layout )
    plotly.offline.iplot(fig) 


def ill_partners_map(partners):
    scl = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'],\
                [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]
    data = [ dict(
            type='choropleth',
            colorscale = scl,
            autocolorscale = False,
            locations = partners[0],
            z = partners[1],
            locationmode = 'USA-states',
            marker = dict(
                line = dict (
                    color = 'rgb(255,255,255)',
                    width = 2
                ) ),
            colorbar = dict(
                title = "Partners Count")
            ) ]

    layout = dict(
            title = 'Interlibary Loan Partners by State<br>(Hover for breakdown)',
            geo = dict(
                scope='usa',
                projection=dict( type='albers usa' ),
                showlakes = True,
                lakecolor = 'rgb(255, 255, 255)'),
                )
        
    fig = dict( data=data, layout=layout )
    plotly.offline.iplot(fig)   
