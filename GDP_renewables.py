#THS PROGRAM SHOWS THE RELATION BETWEEN THE GDP AND THE PRODUCTION OF RENEWABLE
#ENERGIES WITHOUT GOING DEEPER THAN THAT, JUST SHOWS GRAPHS

import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import index  #package created by me

#Get the values of GDP of the given country from 2004 to 2017
def GDP_values(country_study):
    data = pd.read_csv('GDP.csv')
    data.set_index("GDP", inplace=True)
    print(country_study)
    country_GDP=data.loc[country_study]
    print(country_GDP)
    return country_GDP

#Get the percentage of renewable energy generated per year given a country
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

##################################################

years=[2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
country_study=input("Which country do you want to study: ")
#country_study='Greece'

#Find the name of the file
file_name=index.country_file(country_study)

#Asking for all the values of GDP for a country for 2004 to 2017
GDP_year_country=GDP_values(country_study)

#Asking for the percentage of renewable energy for a specific country from 2004 to 2017
renewable_percentage=renewable_percentage_all_years(file_name)

#Repreentation on the same figure of the following curves:
#1.-GDP / years
#2.-Percentage of renewable energy produce / years

fig, ax1 = plt.subplots()
color = 'tab:red'
ax1.set_xlabel('years')
ax1.set_ylabel('GDP in billions of dollars', color=color)
ax1.plot(years, GDP_year_country, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # Second y axis that shares the X axis

color = 'tab:blue'
ax2.set_ylabel('% Renewable Energy Produced', color=color)
ax2.plot(years, renewable_percentage, color=color)
ax2.tick_params(axis='y', labelcolor=color)

plt.show()

#Different way to represent the same data

fig = plt.figure()
fig.suptitle(country_study, fontsize=16)
ax1 = fig.add_subplot(211)
ax1.plot(years,renewable_percentage)
ax1.set_ylabel('Renewable')  # we already handled the x-label with ax1
ax1.grid(True)
ax1.axhline(0, color='black', lw=2)

ax2 = fig.add_subplot(212, sharex=ax1)
ax2.plot(years,GDP_year_country)
ax2.set_ylabel('GDP')
ax2.grid(True)
ax2.axhline(0, color='black', lw=2)

plt.show()
