def clean_data(df):
    df = df.dropna()
    df = df.dropDuplicates()
    return df
