import pandas as pd

def cleaning(df):

    # Fills the missing values at "Rating" with 0, to show that there are no ratings.   
    df["Rating"] = df["Rating"].fillna(0)

    #Drops rows where outliers have been observed.
    # The below row had weird values in more columns, also had rating 19.0
    df = df[df["Reviews"] != "3.0M"]

    # Casts "Reviews" and "Rating" to integer.
    df["Rating"] = df["Rating"].astype(float)
    df["Reviews"] = df["Reviews"].astype(int)

    # Formats "Installs" by removing "," and "+", then casts to integer. 
    df["Installs"] = df["Installs"].str.replace(",", "").str.replace("+", "")
    df["Installs"] = df["Installs"].astype(int)
    
    # Formats "Price" by removing "$", then casts it to float.    
    df["Price"] = df["Price"].str.replace("$","")
    df["Price"] = df["Price"].astype(float)
    
    # Dropping columns that will not be used in the current analysis.   
    df = df.drop(['Current Ver','Android Ver'], axis = 1)
    
    # We only have one Nat, so I filled with the date form the next valid entry...
    df['Last Updated'] = pd.to_datetime(df['Last Updated'], errors='coerce')
    df['Last Updated'].fillna(method='ffill', inplace=True)
    
    return df
