import pandas as pd

def clean_data(df):
    try:
        df = df.drop_duplicates()
        df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors = 'coerce')

        df['TotalAmount'] = pd.to_numeric(df['TotalAmount'], errors = 'coerce')
        df['TotalAmount'] = df['TotalAmount'].round(2)

        df["OrderMonth"] = df['OrderDate'].dt.month
        df["OrderYear"] = df['OrderDate'].dt.year

        return df
    except Exception as e:
        raise Exception(f"Error in clean_data: {str(e)}")
    
    