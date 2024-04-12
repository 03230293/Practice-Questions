arr= [1,2,3,6,9]
def nested_loops(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j]) 
nested_loops(arr)