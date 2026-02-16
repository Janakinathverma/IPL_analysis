import pandas as pd

def clean_data(df):
    """
    Perform basic cleaning:
    - Remove duplicates
    - Handle missing values
    - Standardize column names
    """

    # Standardize column names (lowercase + replace spaces)
    df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Drop rows where match_id is missing (critical column)
    if 'match_id' in df.columns:
        df = df.dropna(subset=['match_id'])

    # Fill remaining numeric NaN with 0
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)

    return df
