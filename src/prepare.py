import pandas as pd
import numpy as np

def prepare_for_correlation(crime_df, chicago_indexes_df, column):
    """
    inputs: A crime DataFrame .
            A DataFrame with the hardship indexes.
            A column of the crime DataFrame.
    output: a DataFrame ready to check correlation of input column with hardship index.
    
    Description: Receives a column of the crime DataFrame and returns new DataFrame that contains the Community Area,
    the total values of the input column and the hardship index. So it's easy to check the correlation of the variable
    with the hardship index.
    """
    chicago_indexes_df.rename({"Community Area Number":"Community Area"}, axis="columns", inplace=True)
    result_df = crime_df[crime_df["Primary Type"] == column]
    result_df = result_df[['ID', 'Date', 'Block', 'Description', 'Location Description', 'Arrest', 'Domestic', 'Beat', 'District', 'Community Area', 'Year', 'Latitude', 'Longitude', 'Location']]
    result_df = pd.DataFrame(result_df["Community Area"].value_counts()).reset_index()
    result_df.rename({"index": "Community Area", "Community Area": f"Total_{column}"}, axis="columns", inplace=True)
    result_df = pd.merge(result_df, chicago_indexes_df[["Community Area", "HARDSHIP INDEX"]], how="inner", on="Community Area")
    result_df.sort_values(by="Community Area").reset_index(drop=True, inplace=True)
    return result_df
    

def calc_correlation(crime_df, chicago_indexes_df, column):
    """
    inputs: A crime DataFrame .
            A DataFrame with the hardship indexes.
            A column of the crime DataFrame.
    output: A float, the correlation of the input column with the hardship index.
    
    Description: Receives a column of the crime DataFrame and returns the correlation of the input column 
    with the hardship index.
    """
    chicago_indexes_df.rename({"Community Area Number":"Community Area"}, axis="columns", inplace=True)
    result_df = crime_df[crime_df["Primary Type"] == column]
    result_df = result_df[['ID', 'Date', 'Block', 'Description', 'Location Description', 'Arrest', 'Domestic', 'Beat', 'District', 'Community Area', 'Year', 'Latitude', 'Longitude', 'Location']]
    result_df = pd.DataFrame(result_df["Community Area"].value_counts()).reset_index()
    result_df.rename({"index": "Community Area", "Community Area": f"Total_{column}"}, axis="columns", inplace=True)
    result_df = pd.merge(result_df, chicago_indexes_df[["Community Area", "HARDSHIP INDEX"]], how="inner", on="Community Area")
    result_df.sort_values(by="Community Area").reset_index(drop=True, inplace=True)
    correlation = result_df.corr().loc["HARDSHIP INDEX",f"Total_{column}"]
    return round(correlation, 3)
    

def create_correlation_df(crime_df, chicago_indexes_df):
    """
    input: A crime DataFrame containing individual crime reports.
    output: A DataFrame with the correlation of each crime with the hardship index.
    """
    correlation_dict = {}
    for crime_type in crime_df["Primary Type"].unique():
        correlation_dict[crime_type] = calc_correlation(crime_df, chicago_indexes_df, crime_type)

    return pd.DataFrame(correlation_dict, index = ["Correlation"]).T.dropna().sort_values(by="Correlation", ascending=False)
    
def prepare_dataframe(crime_df, primary_type):
    """
    input: A crime DataFrame and a primary type of crime.
    output: A DataFrame with limited Latitudes and Longitudes that only has crimes of the selected primary type.
    """
    result_df = crime_df[crime_df["Primary Type"] == primary_type]
    result_df = result_df[(result_df["Latitude"] > 41.5)&(result_df["Latitude"] < 42.1)]
    result_df = result_df[(result_df["Longitude"] > -87.85)&(result_df["Longitude"] < -87.52)]
    return result_df