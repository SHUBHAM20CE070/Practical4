#20CE070_Shubham Panchal
#Find runner-up from given list
#practical4


n = int(input())
arr = map(int,input().split())
arr = list(set(list(arr)))
array_length = len(arr)
arr = sorted(arr)
print(arr[array_length-2])
