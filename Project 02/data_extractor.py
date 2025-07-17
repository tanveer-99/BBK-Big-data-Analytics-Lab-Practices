import pandas as pd
import glob
import json

# Read all .json files in the folder
json_files = glob.glob("audio_output/*.json")
# Load all JSON files into one DataFrame
df = pd.DataFrame()

# columns that we are interested in
columns = [
    "id", "title", "uploader", "artist", "tags", "duration_seconds", "upload_date", "view_count", "like_count", "year_uploaded", "tag_count"
]


for file in json_files:
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        # Ensure it’s always a list of dicts
        records = data if isinstance(data, list) else [data]

        temp_df = pd.DataFrame(records) # convert the list of dictionaries into a dataframe
        temp_df = temp_df[columns] # select only the required columns

        df = pd.concat([df, temp_df], ignore_index=True)

    
print(df.head())
df.to_csv("data/combined_metadata.csv", index=False)