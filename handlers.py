import pandas as pd

def graphGenerator(path: str, window):
    dataframe = pd.read_excel(path, usecols="A:B", header=None)
    numeric_data = dataframe.apply(lambda col: pd.to_numeric(col, errors='coerce')).dropna() 
    force = dataframe.iloc[:,1].tolist()
    deformation = dataframe.iloc[:,0].tolist() 

