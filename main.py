from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/{abcd}")
def root():
    df = pd.read_csv('https://storage.cloud.google.com/get-cooking/dataset/RAW_recipes.csv')
    sample_data = df.head()
    return sample_data.to_csv()