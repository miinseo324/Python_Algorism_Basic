#import sys
#sys.stdin=open("input1.txt", "rt")
n, k=map(int,input().split())
a=[] # 약수를 리스트 a에 저장할 것임

for i in range(n): # n번만큼 반복해서 약수를 찾을 것임
    if n%(i+1)==0: # n을 (i+1)로 나눈 값의 나머지가 0이라면
        a.append(i+1) # 리스트 a에 i+1을 추가할 것임
a.sort() # n의 약수들을 정렬할 것임
print(a)
print(a[k-1])
    
