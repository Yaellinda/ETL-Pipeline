import pandas as pd

def remove_duplicates(df):

    """ a function that takes a DataFrame and removes duplicates"""
    if df.duplicated().sum()>0:
        df_cleaned=df.drop_duplicates(keep='first')
        print("The shape of the data frame without duplicates is :", df_cleaned.shape)
    else:
        df_cleaned=df
        print("this data frame contains no duplicates")
    return df_cleaned
