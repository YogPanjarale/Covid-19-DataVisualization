import pandas as pd
import plotly.express as px
import csv
import os
data = pd.read_csv("csvFiles\covidData.csv")
figure = px.scatter(data,x="date",y="cases",color="country",title="Covid 19 daily cases through time", size ="cases")
# figure = px.line(data,x="date",y="cases",color="country",title="Covid 19 daily cases through time")

figure.show()
input("Press Any key to continue and close")