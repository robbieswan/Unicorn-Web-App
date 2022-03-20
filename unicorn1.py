import csv #import to use the csv module
import pandas as pd
import altair as alt
import plotly.express as px
import altair_saver as a
import streamlit as st


# streamlit run c:/Users/robbi/OneDrive/Desktop/PROJECTS/unicorn1.py

def app():

    with open('Unicorn_Clean.csv', mode="r") as csv_file: #"r" represents the read mode
        reader = csv.reader(csv_file) #this is the reader object

        # for item in reader:
        # # you have to loop through the document to get each data
        #     print(item)

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



    #################################################################################

    # Create a bar grpah showing unicorns by country type


    # country_num = unicorn.loc[unicorn['Country'] == 'China','Country'].sum()
    # print(country_num)

    # china = unicorn[unicorn.Country == 'China']

    # Get value counts for all the countries
    g1 = unicorn.value_counts(unicorn.Country).head(5)

    # Start chart by making the x axis be descending order for country
    # Make the Y axis the count of each country and fade the color scheme to match the amount of instances of that country
    hist = alt.Chart(unicorn, title='Current Unicorns Per Country').mark_bar().encode(
        x = alt.X('Country', sort='-y', title='Country Name'),
        y = alt.Y('count()',title='Amount of Unicorns Per Country'),
        color='count()'
    )

    # Add in the amount count for each country to show on graph
    text = hist.mark_text(
        align='left',
        baseline='middle',
        dy=-10  # Nudges text to right so it doesn't appear on top of the bar
    ).encode(
        text='count()'
    )

    # Combine the text and the first graph 
    final1 = (hist + text).properties(height=560)

    # alt.Chart(china).mark_bar().encode(
    #     x=alt.X('count():Q')
    #     y = 'Valuation ($B)'
    # )

    st.write("""

    ### Per Country
    """)

    # Display the message before the picture
    st.write("""
    The following graph showcases how many current unicorn companies there are per country 
    """)

    # Show the graph on the web application
    st.write(final1)