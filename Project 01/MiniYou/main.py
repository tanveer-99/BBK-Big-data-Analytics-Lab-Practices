import fun

# this is the input data read as a dictionary
input_data = {"data": "datasets/Sleep_health_and_lifestyle_dataset.csv"}
input_data_2 = {"data": "datasets/health_activity_data.csv"}
# the output is stores in this list as needed
data = []

# for row in fun.mini_load_csv_dict(input_data):
#     print(row)
#     break 

for movie in fun.mini_load_csv_yield(input_data):
    data.append(movie)
# print(data)

# -----------------------------

# returns the number of inputs in the column and missing values also
# print(fun.mini_len(input_data, 'Gender'))

#------------------------------

# searches for the specific value in a given column
# print(fun.mini_search(input_data, "Occupation", 'Lawyer'))

# ------------------------------

#calculate the proportion
# print(fun.mini_proportion_count(input_data, "Heart Rates", '70'))

#----------------------------------
# count how many values match between two different column conditions
# print(fun.mini_count_match(input_data, "Occupation", "Doctor", "BMI Category", "Normal"))


# --------------------------------
# takes a numeric column and finds the average
# print(fun.mini_average(input_data, 'Daily Steps'))

#---------------------------
# extracts the Person ID , Quality of Sleep , and Physical Activity Level only for individuals whose occupation is Teacher
# print(list(fun.mini_extract_metrics(input_data, {"Col1":"Person ID", "Col2":"Quality of Sleep", "Col3":"Physical Activity Level"})))

#-------------------------
# this takes min or max and a column name to return the max or min value
# print(fun.mini_states({"Data": input_data, "function": "max", "column": "Age"}))


#-----------------------
# bubble sort in ascending order
# print(fun.mini_bubble_sort({"Data": input_data, "column": "Age"}))

#------------------------------
# finds a specific value in the sorted list
# print(fun.mini_value_list_exists({"Data": input_data, "column": "Age", "value": 29.0}))


#--------------------------------
# counts how many items per category in a specific given column
# print(fun.mini_frequency_table({"Data": input_data, "column": "Gender"}))


#------------------------------
# Check if the Daily_Steps column exists and how many missing values it contains
# print(fun.mini_check_missing_values({"Data": input_data, "column": 'Daily Steps'}))


#-------------------------------
# Count how many individuals report Daily_Steps of 6457 hours.
# print(fun.mini_report_daily_steps(input_data))


#-----------------------------------
# Calculate the average BMI across all individuals
# print(fun.mini_calculate_average_BMI(input_data_2))


#---------------------------------
# how many female users sleep 7.4 hours
# print(fun.mini_count_specific_sleep_based_on_gender({"Data": input_data, "col_one": "Gender", "val_one": "Female", "col_two": "Sleep Duration", "val_two": "7.4"}))
