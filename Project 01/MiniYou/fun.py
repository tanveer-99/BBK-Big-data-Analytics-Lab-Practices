# All the functions must be written in this file
import csv

# this function loads the csv file as dictionary and stores the rows in a list with conventional return statement
def mini_load_csv_dict(input_dict):
    filename = input_dict.get('data')
    if not filename:
        raise ValueError("No 'data' key provided in the input dictionary.")
    data_rows = []
    try:
        with open(filename, "r", newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data_rows.append(row)            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    return data_rows

#-----------------------------------------------
 
# this function loads the csv file as dictionary and stores the rows in a list with yield statement
def mini_load_csv_yield(input_dict):
    filename = input_dict.get("data")

    if not filename:
        raise ValueError("No 'data' key provided in the input dictionary.")

    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                yield row
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 
    
#-------------------------------------------

#  finds the number of records present and missing in a given column
def mini_len(input_data, col):
    count = 0
    missing = 0
    for row in mini_load_csv_yield(input_data):
        if col not in row:
            return {"Exists": False}
        if row[col] in [None, ""]:
            missing += 1
        count += 1
    return {"Exists": True, "Column": col, "Number of records": count, "Number of missing records": missing}

#--------------------------------------------

# search for a specific value in a specific given column, if it exists
def mini_search(input_data, col, value):
    rows = mini_load_csv_dict(input_data)
    if col not in rows[0]: #the column does not exist
        return {"Exists": False, "Column": col, "Value": value}
    for row in rows:
        if value.lower() in row[col].lower():
            return {"Exists": True, "Column": col, "Value": value}    
    # no matches found    
    return {"Exists": False, "Column": col, "Value": value} 

# ----------------------------------------