# DAA-Assignment
PROBLEM STATEMENT:

Implement the solution for the Maximum Sum Array by populating the array of size 14 with non-zero [positive/negative] random numbers.
Comment on the sum, if the first element is positive/negative and the last element is positive/negative.


SOLUTION:

•An array of size n=14 is considered with
	- start index 0 as low
	- last index (n-1=13) as high
	- center of the array i.e.,integer value of (low+high)//2 =6 as mid

•The array is divided into two halves
	- left half from low to mid 
	- right half from mid+1 to high

FIRST APPROACH : By using loops in order to iterate through both  halves of the given array

The solution for the maximum sum subarray problem by using loops is designed in the following way:

	•Two for loops are initialized from the mid position with variables i and j for the left subarray and the right subarray respectively.

	•The first loop keeps on decrementing the value of i in order to go from mid to low and get the maximum sum from the left side.

	•Similarly,the second loop keeps on incrementing the j value to reach from mid+1 to high in order to get the maximum sum from the right side. 

	•The final maximum sum = left_sum + right_sum

CODE :
'''py
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
    
a=[5, 8, -3, 9, 12, -8, 7, 11, -9, 1, -2, 4,-7, 6]
maximumSum(a, 0, len(a)-1 )
'''    

SECOND APPROACH : Divide and Conquer algorithm(Recursion)

The solution for the maximum sum subarray problem by divide and conquer algorithm is designed in the following way:
	
	•Divide the given array into two halves

	•Return the maximum of the following three as the final maximum sum 
		-Maximum subarray sum in left half (Make a recursive call)
		-Maximum subarray sum in right half (Make a recursive call)
		-Maximum subarray sum such that the subarray crosses the midpoint

CODE :

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




CONCLUSION:

For start element = +5 and end element= +6/-6 ,the value of maximum sum is same  i.e., 41
And
For start element =-5 and end element = +6/-6, the value of the maximum sum is the same i.e., 36
The difference between the two maximum sum values i.e., 41 and 36 = 5 i.e, the positive value of the start element.

When the sign of the start element is changed from positive to negative irrespective of the sign of the end element, the value of the maximum sum will be decreased by the value of start element.


