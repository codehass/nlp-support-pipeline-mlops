import pandas as pd

def load_data(filepath):
    """
    Loads data from a CSV file.
    """
    return pd.read_csv(filepath)

def save_data(df, filepath):
    """
    Saves dataframe to a CSV file.
    """
    df.to_csv(filepath, index=False)
