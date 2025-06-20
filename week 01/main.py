
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

#------

if __name__ == "__main__": #this line will allow this code block to run only in this script, not as a module.
  data = [10,20,30,40,50,50,60,80,90,100]
  result = linear_search(data,40)
  print(result)

#------

if __name__ == "__main__":
  data = [10,20,30,40,50,50,60,80,90,100]
  print(data[-1])

#------

def get_it(arr):
    for i in arr:
      return i

if __name__ == "__main__":
  data = [10,20,30,40,50,50,60,80,90,100]
  print(get_it(data))

#------

def sum_elements(arr):
    total = 0
    for num in arr:
        total += num
    return total

if __name__ == "__main__":
  data = [10,20,30,40,50,50,60,80,90,100]
  print(sum_elements(data))

#--------

def count_characters(filename):
  count=0
  with open(filename, 'r') as file:
    for char in file:
      count+=1
            
  return count

if __name__ == "__main__":
  filename = 'file1.txt'
  try:
      counts = count_characters(filename)
      print("Letter counts:", counts)
  except FileNotFoundError:
      print("File not found")



#-------
def reverse1(data):
  reverse=[]
  for i in range(len(data) - 1, -1, -1):
    reverse.append(data[i])
  return reverse

def reverse2(data):
    left, right = 0, len(data) - 1
    while left < right:
        # Swap the elements at the left and right indices
        data[left], data[right] = data[right], data[left]
        left += 1
        right -= 1
    return data

if __name__ == "__main__":
  print(reverse1([1,2,3,4,5]))
  print(reverse2([1,2,3,4,5]))