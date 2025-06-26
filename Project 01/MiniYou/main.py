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



# Part D
locations = [
{"city": "New York", "country": "USA", "lat": 40.7128, "lon": -74.0060},
{"city": "London", "country": "UK", "lat": 51.5074, "lon": -0.1278},
{"city": "Paris", "country": "France", "lat": 48.8566, "lon": 2.3522},
{"city": "Tokyo", "country": "Japan", "lat": 35.6895, "lon": 139.6917},
{"city": "Sydney", "country": "Australia", "lat": -33.8688, "lon": 151.2093},
{"city": "Rio de Janeiro", "country": "Brazil", "lat": -22.9068, "lon": -43.1729},
{"city": "Cape Town", "country": "South Africa", "lat": -33.9249, "lon": 18.4241},
{"city": "Moscow", "country": "Russia", "lat": 55.7558, "lon": 37.6173},
{"city": "Beijing", "country": "China", "lat": 39.9042, "lon": 116.4074},
{"city": "Mumbai", "country": "India", "lat": 19.0760, "lon": 72.8777},
{"city": "Cairo", "country": "Egypt", "lat": 30.0444, "lon": 31.2357},
{"city": "Berlin", "country": "Germany", "lat": 52.5200, "lon": 13.4050},
{"city": "Rome", "country": "Italy", "lat": 41.9028, "lon": 12.4964},
{"city": "Toronto", "country": "Canada", "lat": 43.6510, "lon": -79.3470},
{"city": "Dubai", "country": "UAE", "lat": 25.2048, "lon": 55.2708},
{"city": "Singapore", "country": "Singapore", "lat": 1.3521, "lon": 103.8198},
{"city": "Mexico City", "country": "Mexico", "lat": 19.4326, "lon": -99.1332},
{"city": "Buenos Aires", "country": "Argentina", "lat": -34.6037, "lon": -58.3816},
{"city": "Istanbul", "country": "Turkey", "lat": 41.0082, "lon": 28.9784},
{"city": "Bangkok", "country": "Thailand", "lat": 13.7563, "lon": 100.5018},
{"city": "Nairobi", "country": "Kenya", "lat": -1.2921, "lon": 36.8219},
{"city": "Seoul", "country": "South Korea", "lat": 37.5665, "lon": 126.9780},
{"city": "San Francisco", "country": "USA", "lat": 37.7749, "lon": -122.4194},
{"city": "Jakarta", "country": "Indonesia", "lat": -6.2088, "lon": 106.8456},
{"city": "Madrid", "country": "Spain", "lat": 40.4168, "lon": -3.7038},
{"city": "Lisbon", "country": "Portugal", "lat": 38.7169, "lon": -9.1399},
{"city": "Athens", "country": "Greece", "lat": 37.9838, "lon": 23.7275},
{"city": "Hanoi", "country": "Vietnam", "lat": 21.0285, "lon": 105.8544},
{"city": "Oslo", "country": "Norway", "lat": 59.9139, "lon": 10.7522},
{"city": "Lagos", "country": "Nigeria", "lat": 6.5244, "lon": 3.3792}
]

# find the hottest city
# print(fun.mini_hottest_city(locations))

# find the coldest city
# print(fun.mini_coldest_city(locations))

# cities within the range of 20 and 30 degrees
# print(fun.mini_cities_between_range(locations))


# Show top 5 cities with the highest temperature difference (max - min)
print(fun.mini_highest_temp_diff(locations))