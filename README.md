# Overview

After looking at the data concerning unicorn start ups and their growing prevelance in Utah, I decided to create a data analysis web app of unicorn companies throughout the world and the U.S to put the growth of the Utah unicorn scene in perspective.

I obtained the data set from Kaggle with the link provided before. Although the data required some cleaning, the project was fairly good to use from the get-go.

[Raw Data](https://www.kaggle.com/niekvanderzwaag/unicorn-startups-cleaned)

To create this app to initially show up on my own local host, I was able to use streamlit as the deployment tool. When connected to my github account, the app can be a verified published application.

The purpose of the app is to help peopl visualize the similarities and disparities of what makes start-ups and illustrate the direction the Utah start up scene is headed, in relation to the rest of the nation and world.

[Software Demo Video](https://youtu.be/M4XHYSOtrl4)


# Web Pages

The application is laid out in threee seperate areas (2 viewable areas), with the first being the menu which lists two options of either viewing the data by country, while the other options is viewing the data by U.S city. Both pages are dynamicaly created to showcase actual analysis of data worldwide that shows unicorn companies by location.

# Development Environment

The main tools used for this project were streamlit, and my own local host to view the current web page.

When actually building the data analysis part of my web app, I mainly used python with Pandas and Altair packages. Altair was for the building of the graphs and Pandas was to do the data framing and filtering of data to accurately display.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Streamlit documentation](https://docs.streamlit.io/library/get-started/main-concepts)
* [How to build multiple pages](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4)

# Future Work

Here are a few things that I still am working on and will continue to build on the web applicaion.
* Creating user inputs to allow selection of unicorns by country and city.
* Create a machine learning prediction that allows user input for current company dynamics to see it's probability of unicorn type company growth. We will ask for company start date, current valuation, type of investors, and company industry.
* Change CSS styling to allow user less scrolling when viewing graphs.