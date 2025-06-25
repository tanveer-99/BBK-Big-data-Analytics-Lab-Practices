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
        print(f"Error: File '{filename}' not found. ")
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

#-----------------------------------
# this takes min or max and a column name to return the max or min value
def mini_states(input_data):
    rows = mini_load_csv_dict(input_data.get('Data'))
    func = input_data.get('function').lower()
    col = input_data.get('column')
    if col not in rows[0]:
        return {"Function": func, "Column": col, "Result": None}
    result = None
    for row in rows:
        try: 
            number = float(row.get(col))
        except (TypeError, ValueError):
            continue
        if result == None:
            result = number
        else:
            if func=='min' and number < result:
                result = number
            elif func=='max' and number > result:
                result = number 
    return {"Function": func, "Column": col, "Result": result}      
    

#----------------------------------
# bubble sort in ascending order
def mini_bubble_sort(input_data):
    rows = mini_load_csv_dict(input_data.get('Data'))
    col = input_data.get('column')
    if col not in rows[0]:
        return {"Exists": "False"}
    k = 0
    while k < len(rows):
        try:
            float(rows[k][col])
            k += 1
        except(TypeError, ValueError):
            rows.pop(k)
    for i in range(len(rows)):
        for j in range(i+1, len(rows)-i-1):
            if float(rows[i][col]) > float(rows[j][col]):
                rows[i], rows[j] = rows[j], rows[i]
    sorted = [float(row[col]) for row in rows]
    return {"column": col, "sorted data": sorted}


#-----------------------------
# finds a specific value in the sorted list
def mini_value_list_exists(input_data):
    sorted_data = mini_bubble_sort({"Data": input_data.get("Data"), "column": "Age"})
    sorted_values = sorted_data.get("sorted data")
    if input_data.get('value') in sorted_values:
        return {"Value":input_data.get('value'), "Exists": True}
    else:
        return {"Value":input_data.get('value'), "Exists": False}
    

#--------------------------------
# counts how many items per category in a specific given column
def mini_frequency_table(input_data):
    rows = mini_load_csv_dict(input_data.get("Data"))
    col = input_data.get("column")
    if col not in rows[0]:
        return {"Column": col, "Exists": False}
    result = {}
    for row in rows:
        value = row.get(col)
        if not value or not value.strip():
            continue
        value = value.strip().lower()
        if value in result:
            result[value] += 1
        else:
            result[value] = 1
    return {col:result}


#------------------------------
# Check if the Daily_Steps column exists and how many missing values it contains
def mini_check_missing_values(input_data):
    result = mini_len(input_data.get("Data"), input_data.get('column'))
    return {"Column": result['Column'], "Missing Values": result['Number of missing records']}

#-------------------------------
# Count how many individuals report Daily_Steps of 6457 hours.
def mini_report_daily_steps(input_data):
    total = mini_len(input_data, "Daily Steps").get('Number of records')
    proportion = mini_proportion_count(input_data, "Daily Steps", "7000").get('Proportion')
    return {"Column": "Daily Steps", "Individuals Report": proportion*total}


#-----------------------------------
# Calculate the average BMI across all individuals
def mini_calculate_average_BMI(input_data):
    return mini_average(input_data, "BMI")

#---------------------------------
# how many female users sleep 7.4 hours
def mini_count_specific_sleep_based_on_gender(input_data):
    return mini_count_match(input_data.get("Data"), input_data.get('col_one'), input_data.get('val_one'), input_data.get('col_two'), input_data.get('val_two')).get("Count")


    
