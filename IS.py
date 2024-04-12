def insertion_sort(data):
  """Sorts a list of data using insertion sort algorithm.

  Args:
      data: A list of sortable elements.

  Returns:
      A new list containing the sorted data.
  """

  # Start assuming the first element is already sorted (sorted sub-array)
  for i in range(1, len(data)):
    # Pick the element at index i (unsorted element)
    key = data[i]

    # Compare the element with sorted elements behind it (j represents sorted sub-array)
    j = i - 1
    while j >= 0 and data[j] > key:
      # Shift larger elements one position ahead if the current element is smaller
      data[j + 1] = data[j]
      j -= 1

    # Insert the element at its correct position (after the last element smaller than it)
    data[j + 1] = key

  return data

# Example usage
my_list = [8, 3, 1, 4, 2, 7, 6, 5]
sorted_list = insertion_sort(my_list.copy())  # Avoid modifying the original list

print(f"Sorted list: {sorted_list}")
