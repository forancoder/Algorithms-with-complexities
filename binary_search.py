import matplotlib.pyplot as plt
import numpy as np

def binary_search(arr, item):
  low =0
  high = len(arr)- 1
  steps = 0
  answer = None
  while (low<=high):
    steps += 1
    mid = (low+high)//2
    guess = arr[mid]
    if guess<item:
      low = mid +1
    elif guess>item:
      high = mid -1;
    else:
      answer = mid
      low = high+1
  return answer, steps

def generate_sorted_list(size):
  "Generates a sorted list of integers from 1 to size."
  "The + 1 is because range() is exclusive of the stop value, so to include size, we need to go up to size + 1."
  return list(range(1, size + 1))

list_sizes = []
steps_taken = []

sizes_to_test = list(range(1000,200500,500))
for size in sizes_to_test:
    my_list = generate_sorted_list(size)
    # Search for an element not in the list to get worst-case steps
    result, steps = binary_search(my_list, size + 1)
    steps_taken.append(steps)
    list_sizes.append(size)

plt.plot(list_sizes,steps_taken, color= "red", label ="Binary Search Steps")
plt.xlabel("Input size")
plt.ylabel("Steps taken")

plt.plot(list_sizes, np.log2(list_sizes), color= "blue", label ="log2 function")

plt.legend()
plt.show()
