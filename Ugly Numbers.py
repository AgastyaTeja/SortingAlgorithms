i2 = 0
i3 = 0
i5 = 0
ugly = [0]*150
ugly[0] = 1
next_multiple_of_2 = ugly[i2]*2
next_multiple_of_3 = ugly[i3]*3
next_multiple_of_5 = ugly[i5]*5
 
for i in range(150):
    
    next_ugly_num = min(next_multiple_of_2,next_multiple_of_3,next_multiple_of_5)

    ugly[i] = next_ugly_num
    i = i+1

    if next_ugly_num == next_multiple_of_2:

        i2 = i2+1
        next_multiple_of_2 = next_multiple_of_2*2
    elif next_ugly_num == next_multiple_of_3:

        i3 = i3 + 1
        next_multiple_of_3 = next_multiple_of_3*3

    elif next_ugly_num == next_multiple_of_5:
        i5+=1
        next_multiple_of_5 = next_multiple_of_5*5

print(ugly)
    



