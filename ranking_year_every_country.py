#THIS PROGRAM SHOWS THE PRODUTION OF RENEWABLE ENERGY OF EVERY COUNTRY
#GIVEN A CERTAIN YEAR

import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np



#Returns the value of percentage renewable energy produced for a certain country
#and a certain year
def total_energy_country_year(country,year):
    data = pd.read_csv(country)
    data.set_index("Energy", inplace=True)

    total_renewables=data.loc['Total renewables',str(year)]
    total_energy = data.loc['Total energy',str(year)]
    #Calculation of the percentage
    per=round((float(total_renewables)/float(total_energy))*100,2)

    return per



#########################################################
###MAIN PROGRAM######################################
#######################################################
country_list_files=['BE.csv','BG.csv','CZ.csv','DK.csv','DE.csv','EE.csv','EL.csv','ES.csv','FR.csv','HR.csv','IE.csv','IT.csv','CY.csv','LV.csv','LT.csv','LU.csv','HU.csv','MT.csv','NL.csv','AT.csv','PL.csv','PT.csv','RO.csv','SI.csv','SK.csv','FI.csv','SE.csv','UK.csv','NO.csv','IS.csv']
country_names=['Belgium','Bulgaria','Czechia','Denmark','Germany','Estonia','Greece','Spain','France','Croatia','Ireland','Italy','Cyprus','Latvia','Lithuania','Luxembourg','Hungary','Malta','Netherlands','Austria','Poland','Portugal','Romania','Slovenia','Slovak Republic','Finland','Sweden','United Kingdom','Norway','Iceland']
years=[2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
country_short_names=['BE','BG','CZ','DK','DE','EE','EL','ES','FR','HR','IE','IT','CY','LV','LT','LU','HU','MT','NL','AT','PL','PT','RO','SI','SK','FI','SE','UK','NO','IS']


#Asking for the year that we want to study
year_under_study=int(input("Introduce year that you wish to study: "))


#Creates a vector with the values of the percentage of renewable energy produced
#in a determined year, every position of this vector represents the percentage
#produced in a determined country
val_of_the_year_every_country=[]
for i in country_list_files:
    value=total_energy_country_year(i,year_under_study)
    val_of_the_year_every_country.append(value)
print('Legend for better understading of countries abbreviations ')
for i in range(len(country_short_names)):
    print(str(i)+'.- '+country_short_names[i]+' = '+country_names[i])

#Graphic Representation
plt.rcParams['figure.figsize'] = (9.0, 9.0)
x_pos = np.arange(len(country_names))
plt.bar(x_pos, val_of_the_year_every_country, align='center', alpha=0.5)
plt.xticks(x_pos, country_short_names)
plt.ylabel('Renewable Percentage')
plt.grid(True)
plt.title(year_under_study)
plt.show()
