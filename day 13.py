def counting_sort(arr):
  """
  Sorts an array of 0s, 1s, and 2s in ascending order using counting sort.

  Args:
    arr: The array to be sorted.

  Returns:
    A new array containing the sorted elements.
  """

  counts = [0, 0, 0]  
  for number in arr:  
    counts[number] += 1  

  sorted_arr = []  
  for i in range(3):  
    sorted_arr.extend([i] * counts[i]) 

  return sorted_arr

user_input = input("Enter the numbers in the array, separated by spaces: ")
arr = [int(number) for number in user_input.split()]  

sorted_arr = counting_sort(arr)

print("The sorted array is:", sorted_arr)
