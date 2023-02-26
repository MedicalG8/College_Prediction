# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 17:18:04 2023

@author: romil
"""

import pandas as pd
df = pd.read_excel ('compl.xlsx')
df.head()

from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit():
    # Load the data from the Excel file
    df = pd.read_excel('compl.xlsx')

    # Get the user's input from the form
    rank = int(request.form['rank'])
    category = request.form['category']

    # Create an empty list to store the matched colleges
    matched_colleges = []

    # Loop through each row in the dataframe and check if the user's rank and category match
    for i, row in df.iterrows():
        if row['Cat'] == category and row['Cut off Rank 2022'] >= rank:
            matched_colleges.append(row['Name'])

    # Render the results template and pass in the matched colleges
    return render_template('results.html', colleges=matched_colleges)
