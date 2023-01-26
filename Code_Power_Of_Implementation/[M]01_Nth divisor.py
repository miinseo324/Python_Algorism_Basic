N, K = map(int, input("").split())
# N과 K를 입력받음
a=[]

for i in range(N): # N번 반복한다.
    if N%(i+1)==0: # N을 1부터 ~나눴을때 나머지가 0이면
        a.append(i+1)
        #리스트 a에 추가한다.
print(a[K-1])
        
