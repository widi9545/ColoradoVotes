# -*- coding: utf-8 -*-
"""
Author - William Diment
Email: william.j.diment@gmail.com preferred, otherwise widi9545@colorado.edu
Project Begin Date 10/8/20
Purpose: Develop a website showing reported Colorado voter ballot returns for 2020 General Election according to
county and party affiliation 

"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output, State
from sys import stdout 
import datetime
import os
import pandas as pd
import numpy
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)


server = app.server

app.config['suppress_callback_exceptions'] = True



tab_height = '25px'
tab_style = {'height': tab_height, 'padding': '0'}
tablet_style = {'line-height': tab_height, 'padding': '0'}

dataButtonStyle={'padding':'5x', 'text-align': 'center', 'line-height':'5'}

currentDate = datetime.datetime.now()

currentDay = currentDate.strftime('%d')

yesterDay = currentDate - datetime.timedelta(days=1)
yesterDay = yesterDay.strftime('%d')

currentMonth = currentDate.strftime('%m')


default_start_day = currentDay
default_end_day = yesterDay



#yearmarks = {y: {'label': y} for y in yearList } 
#monthmarks = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
#              7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
#daymarks={d: {'label':d } for d in dayList}


#monthoptions = [{'label': monthmarks[i], 'value': i} for i in range(1, 13)]

#months_slanted = {i: {'label': monthmarks[i],
#                      'style': {"transform": "rotate(45deg)"}} for i in months}


navbar = html.Nav(id='first_nav_top')            



body = html.Div([], className='ten columns offset-by-one')

app.layout = html.Div([navbar,body])


if __name__=='__main__':
    app.run_server(debug=True)