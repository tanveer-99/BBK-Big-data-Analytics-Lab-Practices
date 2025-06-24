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

# proportion of a specific value within a given column
def mini_proportion_count(input_data, col, value):
    count = 0
    total = 0
    rows = mini_load_csv_dict(input_data)
    if col not in rows[0]:
        return {"Exists": False}
    for row in rows:
        total += 1
        if value == row.get(col):
            count += 1
        
    proportion_value = count/total
    return {"Exists": True, "Column": col, "Value": value, "Proportion": proportion_value}

#--------------------------------------------

# count how many values match between two different column conditions
def mini_count_match(input_data, col_one, val_one, col_two, val_two):
    count = 0
    rows = mini_load_csv_dict(input_data)
    if col_one not in rows[0].keys() or col_two not in rows[0].keys():
        return {"Exists": False}
    for row in rows:
        if (row.get(col_one) == val_one) and (row.get(col_two) == val_two):
            count += 1
    if count == 0:
        return "columns exist but no match between them"
    return {"Conditions": {col_one: val_one, col_two: val_two}, "Count": count}
    
# -------------------------------
# takes a numeric column and finds the average
def mini_average(input_data, col):
    total = 0.0
    count = 0
    rows = mini_load_csv_dict(input_data)
    if col not in rows[0].keys():
        return {"Exists": False, "Column": col}
    for row in rows:
        try:
            total += float(row.get(col))
            count += 1
        except (TypeError, ValueError):
            continue
    return {"Exists": True, "Column": col, "Average": round(total/count, 2)}

#----------------------------------
# extracts the Person ID , Quality of Sleep , and Physical Activity Level only for individuals whose occupation is Teacher
def mini_extract_metrics(input_data, columns):
    for row in mini_load_csv_yield(input_data):
        if row.get("Occupation").lower() == 'teacher':
            yield {
                columns.get('Col1'): row.get(columns.get('Col1')),
                columns.get('Col2'): row.get(columns.get('Col2')),
                columns.get('Col3'): row.get(columns.get('Col3'))
            }