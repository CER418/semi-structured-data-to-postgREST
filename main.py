import json
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# Define postgresql database
engine = create_engine('postgresql://localhost:5432/postgres')


def json_to_df(json_file):
    """Convert json to pandas dataframe"""
    with open(json_file) as file:
        data = json.load(file)
        return pd.DataFrame.from_dict(data)


def json_to_csv(json_file, csv_output):
    """Convert json to csv"""
    dataframe = json_to_df(json_file)
    return dataframe.to_csv(csv_output)


def df_to_sql(dataframe, table_name):
    """Convert dataframe and insert as sql"""
    return dataframe.to_sql(table_name, engine, if_exists='append',
                            dtype={"index": sqlalchemy.types.JSON, "widget": sqlalchemy.types.JSON})


if __name__ == '__main__':
    df = json_to_df('cars.json')
    df_to_sql(df, 'cars')
