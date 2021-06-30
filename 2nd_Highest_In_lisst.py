# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up
# Sample Input :
#
# 5
# 2 3 6 6 5
# Sample Output :
#
# 5

n = int(input())
arr = map(int, input().split())
arr=set(arr)
arr=list(arr)
arr.sort()
#finding second highest elemnt in scores list
print(arr[-2])



