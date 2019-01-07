def Partition(array,start,end):
    pivot=array[end] #selecting last element as pivot
    pindex=start
    for i in range(start,end):
        if (array[i]<=pivot):
            array[pindex],array[i]=array[i],array[pindex]
            pindex+=1
    array[end],array[pindex]=array[pindex],array[end]
    return(pindex)

def QuickSort(array,start,end):
    if (start<end):
        
        pindex=Partition(array,start,end)
        QuickSort(array,start,pindex-1)
        QuickSort(array,pindex+1,end)

array=[7,2,1,6,8,5,3,4]
QuickSort(array,0,7)
print(array)