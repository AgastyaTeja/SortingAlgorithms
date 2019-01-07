import matplotlib.pyplot as plt

def BubbleSort(array):
    for i in range(len(array)):
        flag=0
        for j in range(len(array)-1-i):
            if(array[j]>array[j+1]):
                array[j],array[j+1]=array[j+1],array[j] #swapping
                flag=1
        if flag==0:# all elements are sorted, no further comparisons required.
            print("Sorted array", array) 
            break
        print(array)
BubbleSort([5,4,3,2,1])

    



