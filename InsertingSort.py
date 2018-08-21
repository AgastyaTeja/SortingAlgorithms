def InsertionSort(array):
  for i in range(1,len(array)): # iterating from second element as 1st is sorted

    value=array[i] 
    temp=i
    while(temp>0 and array[temp-1]>value):
      array[temp]=array[temp-1] #shifting holes/values
      temp=temp-1
    array[temp]=value # condition broke and hole fixed. put the value there

  print(array)
print("7, 10, 3, -4")
InsertionSort([7, 10, 3, -4])
# 1- Memory Saved as new array is not formed.
# 2- Worse case O(n^2) worser for longer numbers
# 3- Best case O(n)
