def cross_sum(A,low,mid,high):
    sum=0
    leftsum=-1000;
    #for the LHS elements of mid 
    for i in range(mid,low-1,-1):
        sum=sum+A[i]
        if (sum>leftsum):
            leftsum=sum
            

    #for the RHS elements of mid
    sum=0
    rightsum=-1000; 
    for i in range (mid+1,high+1):
        sum=sum+A[i]
        if (sum>rightsum):
           rightsum=sum
           
         
    return max(leftsum + rightsum ,leftsum,rightsum)
    


def maximum_sum_subarray(A,low,high):
    if (low>high):
      return -9999999
        
    if (high==low):     
      return A[low]
  
    else:   
      mid=(low + high)//2 
      return max(maximum_sum_subarray(A, low, mid-1), maximum_sum_subarray(A, mid+1, high),cross_sum(A, low, mid, high))
    
      #Maximum subarray sum in left half------------------------------------>maximum_sum_subarray(A, low, mid-1)
      #Maximum subarray sum in right half----------------------------------->maximum_sum_subarray(A, mid+1, high)
      #Maximum subarray sum such that the subarray crosses the midpoint----->mid_sum(A, low, mid, high)
    
      
a = [5, 8, -3, 9, 12, -8, 7, 11, -9, 1, -2, 4,-7,6]
maximum_sum = maximum_sum_subarray(a,0,len(a)-1); 
print("Maximum sum : " ,maximum_sum)

