import fun

input_data = {"data": "datasets/Sleep_health_and_lifestyle_dataset.csv"}
data = []

# for row in fun.mini_load_csv_dict(input_data):
#     print(row)
#     break 

for movie in fun.mini_load_csv_yield(input_data):
    data.append(movie)

print(data[0])
print(fun.mini_len(input_data, 'Gender'))

