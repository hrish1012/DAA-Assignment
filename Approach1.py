
def maximumSum(arr,low,high):

    left_sum=-9999999999
    right_sum=-9999999999 
    suml=0
    sumr=0
    maxLeft=-1
    maxRight=-1
    mid=(low+high)//2
    
    #for left half of the array
    for i in range(mid,low-1,-1):
        suml = suml+arr[i]
        if(suml>left_sum):
            left_sum=suml
            maxLeft=i
        
    
    #for right half of the array
    for j in range(mid+1,high+1,1):
        sumr=sumr+arr[j]
        if(sumr>right_sum):
            right_sum=sumr
            maxRight=j
    
    print(a)
    print("Maximum sum subarray : ",arr[maxLeft:maxRight + 1])    
    print("Maximum sum : ", (left_sum+right_sum))
    print("Start index : ",(maxLeft))
    print("End index   : ",maxRight)
    
a=[-7, 8, -3, 9, 12, -8, 5, 11, -9, 1, -2, 4,-5,-6]
maximumSum(a, 0, len(a)-1 )
    
