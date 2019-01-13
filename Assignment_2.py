# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 13:05:38 2018

@author: Serap Aydogdu-528181041
"""
#Solutions of Midterm by 09/12/2018
#%%
def problem1(datafile="C:/Users/orhan aydogdu/Desktop/Advances in Data Science/homeworks/hw-2/midterm-data/BreadBasket_DMS.csv"):
    import pandas as pd
    import numpy as np
    
    data=pd.read_csv(datafile,encoding="latin-1")
    #a) Print the number of unique items
    print("the number of unique items:",len(data["Item"].unique()))  
    #b) Print how many times each item was sold
    df=pd.DataFrame(data["Item"].value_counts())    
    df.index.name="Item"                                        #give index name 
    df.columns=['Quantity Sold']                                #give column a name
    print(df.head(5))   #b)    
    #c) How many transaction contain Coffee
    print("the number of transactions that have Coffee is",data[data["Item"]=="Coffee"].groupby(["Transaction"]).count().shape[0])
   
  
#%%
def problem2(datafile="C:/Users/orhan aydogdu/Desktop/Advances in Data Science/homeworks/hw-2/midterm-data/country_population.csv"):
    import pandas as pd
    import numpy as np
    
    data=pd.read_csv(datafile,encoding="latin-1")
    #a) Print 10 countries having at least number of population in 2016
    df=data.loc[:,["Country Name", "2016"]];                     #retrieve "Country Name" and "2016" columns from data and assign to new dataframe named df.
    df=df.sort_values(by=["2016"], ascending=True)[:10].reset_index(drop=True);          #sort values basis on 2016 by descending order.Print only 10 countries and reset indexes of them.
    df.index = np.arange(1,len(df)+1);                           #for index starting from 1 to 10 create a numpy array which stars from 1.
    print(df,'\r\n '*5)         
    #b) Calcualte the percentage increase of the 2016 populations compared to 2010 populations.Print the top-ten countries having highest increase
    df2=data.loc[:,["Country Name", "2010","2016"]]              #retrieve "Country Name" and "2016" columns from data and assign to new dataframe named df2.   
    df2["Percentage Increase"]=abs((df2["2010"]-df2["2016"])/df2["2010"])*100      #calculate the percentage increase btw 2016 to 2010. absulute is beng used for negative values.
    df2=df2.sort_values(by= ["Percentage Increase"], ascending=False)[:10].reset_index(drop=True)      #Then sort the df2 basis on "Percentage Increase" column from high to low. For ten top countries filter the data [:10]
    df2.index = np.arange(1,len(df2)+1)       #for index starting from 1 to 10 create a numpy array which stars from 1. 
    print(df2,'\r\n '*5)
    #c) Do the same task asked in above but this time only for the countries that have more than 10 million population
    df3=data.loc[:,["Country Name", "2010","2016"]]
    df3["Percentage Increase"]=abs((df3["2010"]-df3["2016"])/df3["2010"])*100        #calculate the percentage increase btw 2016 to 2010. absulute is beng used for negative values.
    df3=df3[(df3["2010"]> 10000000) & (df3["2016"]> 10000000)].sort_values(by= ["Percentage Increase"], ascending=False).reset_index(drop=True)[:10]       #at that time filter data of 2010 and 2016 basis on coutries population which are greater than 10M.
    df3.index=np.arange(1,len(df3)+1);              #for index starting from 1 to 10 create a numpy array which stars from 1. 
    print(df3,'\r\n '*5)
    #Find the year that world population has the highest incerased compared to previous year.
    data.set_index("Country Name", inplace=True)
    df_world=data.loc["World"]
    df_world=df_world.drop(labels=['Country Code','Indicator Name','Indicator Code'])        #This is a Series.
    df_world=pd.DataFrame(df_world)                         # convert into a DataFrame
    df_world["df_world_perc"]=df_world["World"].pct_change()*100
    year=df_world["df_world_perc"].idxmax()
    value=df_world["df_world_perc"].max()
    print(year,"has the highest percentage increase, which is ",value)
    
#%%
def problem3(datafile="C:/Users/orhan aydogdu/Desktop/Advances in Data Science/homeworks/hw-2/midterm-data/norway_new_car_sales_by_model.csv"):
    import pandas as pd
    import numpy as np
   
    data=pd.read_csv(datafile,encoding="latin-1")
    data["Make"]=data["Make"].str.replace('\xa0Mercedes-Benz ','Mercedes-Benz ')       #delete some digits from in front of Mercedes-Benz
    data.Make=data.Make.str.lower()        #make all characters lower in Make column.
    data.Model=data.Model.str.lower()      #make all characters lower in Model column.
    
    def f1(data_x):        
        data_x=data_x.groupby(["Year","Model"])[["Quantity"]].sum()                    #group by both Year and Model and take the sum of Quantity of each group
        return data_x.std(level=1).sort_values(by="Quantity", ascending=False)[:1]     #then sort by Quantity basis on standard deviation of Model.
        
    data_f1=data.groupby("Make").apply(f1)         #group by Make column and apply f1 function to each producer.
    data_f1=data_f1.query("Quantity != 'NaN'")     #take out values which are not fluctuated. (standard deviation = NaN )
    #For printing out as regarded in assignment:
    data_f1=data_f1.reset_index(level=[0,1])       #we had multi-index. So first breaking out multi index in the data.
    data_f1=data_f1[['Make','Model']]              #take only Make and Model columns
    data_f1.set_index('Make',inplace=True)         #then set Make as an index.
    print(data_f1)    
#%%    