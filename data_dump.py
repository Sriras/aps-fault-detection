import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

# Dataset path
data_file_path = "/config/workspace/aps_failure_training_set1.csv"

# Database name
Database_name = "aps"

# collection name
Collection = 'sensor'


if __name__ == "__main__":
    
    # Read the dataset
    df = pd.read_csv(data_file_path)
    rows, column = df.shape
    print("Rows - {} Columns - {}".format(rows, column))

    # convert dataframe to json 
    df.reset_index(drop=True, inplace=True)

    json_records = list(json.loads(df.T.to_json()).values())


    # Insert data into json

    client[Database_name][Collection].insert_many(json_records)