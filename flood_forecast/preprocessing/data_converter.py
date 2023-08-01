"""
A set of function aimed at making it easy
to convert other time series datasets to our
format for transfer learning purposes
"""


def make_column_names(df):
    num_cols = len(list(df))
    column_arr = [f"solar_{str(i)}" for i in range(0, num_cols)]
    # ensure the length of the new columns list is equal to the length of df's columns
    df.columns = column_arr
    return df
