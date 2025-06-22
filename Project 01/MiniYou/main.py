import fun

input_data = {"data": "datasets/health_activity_data.csv"}

# for row in fun.mini_load_csv_dict(input_data):
#     print(row)
#     break 

for movie in fun.mini_load_csv_yield(input_data):
    print(movie)