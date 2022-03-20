import csv #import to use the csv module
import pandas as pd
import altair as alt
import plotly.express as px
import altair_saver as a
import streamlit as st

# streamlit run c:/Users/robbi/OneDrive/Desktop/PROJECTS/unicorn2.py

def app():

    with open('Unicorn_Clean.csv', mode="r") as csv_file: #"r" represents the read mode
        reader = csv.reader(csv_file) #this is the reader object


    st.write("""
    # Unicorn Company Visualizer
    ---
    """)

    unicorn = pd.read_csv('Unicorn_clean.csv',encoding = "Latin-1")

    # print(unicorn)
    # unicorn


    utah_companies = unicorn.loc[(unicorn['City'] == 'Lehi') | (unicorn['City']=='Salt Lake City')]
    # print(utah_companies)


    # Count the amount of NA in dataframe
    # unicorn.isna().sum()

    # Drop the unnamed investors in the last column
    unicorn.drop(['Unnamed: 0','Investor 4'],axis=1,inplace= True)


    #########################################################################################

    # Create a graph that shows which cities inside the United States have the most unicorns

    # cities = unicorn.loc[unicorn['City'] == 'China','Country'].sum()
    cities = unicorn.loc[unicorn.Country == 'United States']

    # How to create data frame that only creates certain cities.
    # new = cities.loc[(cities['City'] == 'Lehi') | (cities['City'] == 'Salt Lake City')]

    # new1 = cities.loc[(cities['City'] == 'Lehi/Salt Lake City')]

    histogram = alt.Chart(cities, title='Current Unicorns Per City').mark_bar().encode(
        x = alt.X('City', sort='-y', title='City Name'),
        y = alt.Y('count()',title='Amount of Unicorns Per City'),
        color='count()'
    )

    # hist2 = alt.Chart(new2).mark_bar(color='orange').encode(
    #     x = alt.X('City', sort='-y', title='City Name'),
    #     y = alt.Y('count()',title='Amount of Unicorns Per City')
    # )

    text3 = histogram.mark_text(
        align='left',
        baseline='middle',
        dy=-10 # Nudges text to right so it doesn't appear on top of the bar
    ).encode(
        text='count()'
    )

    final2 = (histogram + text3).properties(height=600)


    st.write("""
    ### Per City (U.S)
    """)

    # Display the message before the picture
    st.write("""
    The following graph showcases how many current unicorn companies there are per city within
    the United States. Please note, cities with less than 2 unicorn company may not be shown.
    """)


    # Show graph depicting companies by U.S City
    st.write(final2)