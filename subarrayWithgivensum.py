#sliding window question

def subArraySum(arr,n,sum_):
    #curr_sum array ka pehla value
    curr_sum=arr[0]
    start=0

    i=1 # one se chaloo karo kyoki 0 use ho gaya

    while i<=n:
        while curr_sum>sum_ and start<i-1:
            curr_sum=curr_sum-arr[start]
            start+=1
        
        if curr_sum==sum_:
            print("sum found between index")
            print("%d and %d "%(start,i-1))
            return 1
        if i<n:
            curr_sum=curr_sum+arr[i]
        i+=1

    print('no subarray found')
    return 0

arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum_ = 23
 
subArraySum(arr, n, sum_)
