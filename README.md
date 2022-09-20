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


SECOND APPROACH : Divide and Conquer algorithm(Recursion)

The solution for the maximum sum subarray problem by divide and conquer algorithm is designed in the following way:
	•Divide the given array into two halves

	•Return the maximum of the following three as the final maximum sum 
		-Maximum subarray sum in left half (Make a recursive call)
		-Maximum subarray sum in right half (Make a recursive call)
		-Maximum subarray sum such that the subarray crosses the midpoint



CONCLUSION:

For start element = +5 and end element= +6/-6 ,the value of maximum sum is same  i.e., 41
And
For start element =-5 and end element = +6/-6, the value of the maximum sum is the same i.e., 36
The difference between the two maximum sum values i.e., 41 and 36 = 5 i.e, the positive value of the start element.

When the sign of the start element is changed from positive to negative irrespective of the sign of the end element, the value of the maximum sum will be decreased by the value of start element.


