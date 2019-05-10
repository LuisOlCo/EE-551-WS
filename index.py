country_list_files=['BE.csv','BG.csv','CZ.csv','DK.csv','DE.csv','EE.csv','EL.csv','ES.csv','FR.csv','HR.csv','IE.csv','IT.csv','CY.csv','LV.csv','LT.csv','LU.csv','HU.csv']
country_names=['Belgium','Bulgaria','Czechia','Denmark','Germany','Estonia','Greece','Spain','France','Croatia','Ireland','Italy','Cyprus','Latvia','Lithuania','Luxembourg','Hungary']
years=[2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]

def index_year(year):
    for i in range(len(years)):
            if year==years[i]:
                pos=i
    return pos

def country_file(country):
    for i in range(len(country_names)):
        if country==country_names[i]:
            pos_file_name=i
    return country_list_files[pos_file_name]
