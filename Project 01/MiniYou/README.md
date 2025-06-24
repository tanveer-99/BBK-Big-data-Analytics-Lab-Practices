# Part A: Warmup Tasks
## Folder Structure


```
MiniYou
├── fun.py
├── main.py
├── README.md
└── datasets
    ├── health_activity_data.csv
    └── Sleep_health_and_lifestyle_dataset.csv
```
## Datasets
The two datasets are discussed below:
### health_activity_data.csv
//comment on the dataset
### Sleep_health_and_lifestyle_dataset.csv
//comment on the dataset

## Functions
### mini_load_csv_dict()

The function takes the csv dataset as a dictionary and loads it with the ` csv.DictReader() `. This function uses the return method to return all the rows in a single list. 

```python def mini_load_csv_dict(input_dict):
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
```

Time complexity: ` O(n) `: looping over every row once, which is  O(1), so O(n). </br>
Space complexity: ` O(n) `: creating the list makes it take the same space as the rows in the dataset.

### mini_load_csv_yield()
This function does the same with the ` yield ` method.

```python
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
```

Time complexity: ` O(n) `: same as the return method
<br/>
Space complexity: ` O(1) `: we process one at a time and not using any list. so does not need extra spaces.

# Part B
## Task 01
` mini_len() ` function that takes a column name as input and returns: </br>
1. Whether the column exists in the dataset ( Exists: True or False )
2. If it exists:
    1. name of the column
    1. number of records
    1. number of missing values

Usage:

```python
input_data = {"data": "datasets/Sleep_health_and_lifestyle_dataset.csv"}
print(fun.mini_len(input_data, 'Gender'))
```

Output: </br>
If exists:
` {"Exists": True, "Column": "Gender", "Number of records": 374, "Number of missing
records": 0} ` <br/>
if not exists;
`{"Exists": False}`

Time complexity:` O(n)`, as each row is processed on by one <br/>
Space complexity: `O(1)`, one row at a time from the generator, no need of extra spaces.

## Task 02
`mini_search()` function takes the dataset and a column name and the value as input, searches for it and returns if it exists or not
> Here `return` is used as we want to exit immediately upon finding the first match

Usage:
```python
print(fun.mini_search(input_data, "Occupation", 'Lawyer'))
```

Output:
</br>
If exists: ` {"Exists": True, "Column": "Occupation", "Value": "Lawyer"} `
</br>
If not exists: ` {"Exists": False, "Column": "Occupation", "Value": "Lawyer"}  `

Time: `O(n)`

Space: `O(n)`

## Task 03
` mini_proportion_count() ` takes the column name and value as input and finds the proportion of the value in the entire column. The proportion is calculated as follows: if 3 out of 10 rows have the value "Engineer", the proportion is 3/10 = 0.3.

> `return` is used intead of `yield` as we need to traverse through everything and give a final aggregated value, rather than processing one by one

Usage:
```python
print(fun.mini_proportion_count(input_data, "Heart Rate", '70'))
```

Output:
<br/>
If exists: `{'Exists': True, 'Column': 'Heart Rate', 'Value': '70', 'Proportion': 0.20320855614973263}`
<br/>
If not exists: `{'Exists': False}`

Time complexity: `O(N)`
<br/>
Space complexity: `O(N)`
