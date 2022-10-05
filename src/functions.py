import pandas as pd

def create_df():
    
    df = pd.read_csv('../data/life-expectancy.csv')
    
    df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]
    
    return df