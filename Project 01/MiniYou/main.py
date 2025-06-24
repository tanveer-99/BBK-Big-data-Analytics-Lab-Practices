import fun

# this is the input data read as a dictionary
input_data = {"data": "datasets/Sleep_health_and_lifestyle_dataset.csv"}
# the output is stores in this list as needed
data = []

# for row in fun.mini_load_csv_dict(input_data):
#     print(row)
#     break 

for movie in fun.mini_load_csv_yield(input_data):
    data.append(movie)
# print(data[0])

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

