def BinarySearch(array,targetvalue,flag=0):
    min=0
    max=len(array)-1
    while(max>min):
        guess=int((array[max]+array[min])/2)
        if array[guess]==targetvalue:
            print("found at"+str(guess))
            flag=1
            break
        elif array[guess]<targetvalue:
            min=guess+1
        else:
            max=guess-1
    
    if flag==0:
        print("Your Element is not found")

BinarySearch([1,2,3,4],5,flag=0)


