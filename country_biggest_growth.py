
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import index  #package created by me


#Get the values of GDP of the given country from 2004 to 2017
def GDP_values(country_study):
    data = pd.read_csv('GDP.csv')
    data.set_index("GDP", inplace=True)
    country_GDP=data.loc[country_study]
    n=len(country_GDP)
    GDP=[]
    for i in range(n):
        GDP.append(country_GDP[i])

    return GDP

#Get the percentage of renewable energy generated per year
def renewable_percentage_all_years(file_name):

    data = pd.read_csv(file_name)
    data.set_index("Energy", inplace=True)
    #Find the total renewable energy generated by the country
    total_renewables=[]
    for i in data.loc['Total renewables']:
        total_renewables.append(i)
    #Find the total energy generated by the country (renewables and not renewables)
    total_energy=[]
    for i in data.loc['Total energy']:
        total_energy.append(i)

    #Compute the total percentage of renewable energy generated from the total energy generated by the country
    percentage=[]
    for t in range(len(years)):
        per=round((float(total_renewables[t])/float(total_energy[t]))*100,2)
        percentage.append(per)

    return percentage

# Compute the gradient descent algorithm
def gradient_descent_algorithm(X,Y):
    # Building the model
    m = 0
    c = 0
    L = 0.00001  # The learning Rate
    epochs = 100000
    n = float(len(X)) # Number of elements in X
    # Performing Gradient Descent
    for i in range(epochs):
        Y_pred = m*X + c  # The current predicted value of Y
        D_m = (-2/n) * sum(X * (Y - Y_pred))  # Derivative wrt m
        D_c = (-2/n) * sum(Y - Y_pred)  # Derivative wrt c
        m = m - L * D_m  # Update m
        c = c - L * D_c  # Update c

    print (m, c)

    return m, c

##################################################
country_list_files=['BE.csv','BG.csv','CZ.csv','DK.csv','DE.csv','EE.csv','EL.csv','ES.csv','FR.csv','HR.csv','IE.csv','IT.csv','CY.csv','LV.csv','LT.csv','LU.csv','HU.csv']
country_names=['Belgium','Bulgaria','Czechia','Denmark','Germany','Estonia','Greece','Spain','France','Croatia','Ireland','Italy','Cyprus','Latvia','Lithuania','Luxembourg','Hungary']
years=[2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
growth_RE_all_countries=[]

for i in country_names:
    country_study=i

    #Find the name of the file
    file_name=index.country_file(country_study)

    #Asking for all the values of GDP for a country for 2004 to 2017
    GDP_year_country=GDP_values(country_study)

    #Asking for the percentage of renewable energy for a specific country from 2004 to 2017
    renewable_percentage=renewable_percentage_all_years(file_name)


# Compute of the GDP growth and production of reneable energy.
# The GDP growth during 2005 would be: (GDP of 2005 - GDP of 2004) / 1year
# Same operation to determine the Renewable Energy poduction growth

    n=len(GDP_year_country)
    tasa_GDP=[0]
    for i in range(n-1):
        tasa_GDP.append(round(GDP_year_country[i+1]-GDP_year_country[i],2))

    tasa_renewable=[0]
    for i in range(n-1):
        tasa_renewable.append(round(renewable_percentage[i+1]-renewable_percentage[i],2))


# Finds the delay between the GDP and the and the growth of renewable energy production
    delay=np.correlate(tasa_renewable,tasa_GDP,mode='full')
    lag=delay.argmax()-(len(tasa_GDP)-1)


#We now take the growth measure for the GDP and the renewable energy percentage
#production and we represent it, but first we have to align both vectors given the
#delay stablished

#We us de the for loops to aligned both vectors
    for i in range (lag):
        tasa_renewable.pop(0)

    for i in range (lag):
        tasa_GDP.pop(-1)


#We stablished now the gradient descent algorithm for showing the correlation between
#GDP and RE(renewable energy) production


    X = pd.array(tasa_GDP)
    Y = pd.array(tasa_renewable)


    m, c=gradient_descent_algorithm(X,Y)

# Making predictions
    Y_pred = m*X + c


###########################################################################
# Once we have determined the equation that describes the correlation between
# growth of the GDP and the growth of RE generation we can predict what it is going to be
# the growth of the RE production during 2019

# Variable n represents the position, starting from the right side of the vector,
# that contains the value of the GDP in the year of interest given the lag

    n = 2-lag-1

    delta_GDP= GDP_year_country[n] - GDP_year_country[n-1]
    delta_RE_production = delta_GDP*m + c
    print(delta_RE_production)
    growth_RE_all_countries.append(delta_RE_production)

print(growth_RE_all_countries)

growth_RE_all_countries=np.array(growth_RE_all_countries)
max=np.argmax(growth_RE_all_countries)

print('The country that will growth bigger its production of renewable energy is: ' + str(country_names[max]))
