N, M = map(int, input().split()) # 두 개의 정 다면체 자연수를 입력받는다.
sum=[] # 여기에는 나올 수 있는 합들을 모두 저장할거다.
for i in range(1,N+1): # for 문 돌려서 다 저장한다.
    for j in range(1, M+1):
        sum.append(i+j)

cnt=[] # cnt 에다가 각각의 수들이 몇개씩 나왔는지 세서 저장한다. 
for i in range(2,N+M+1):# 2부터 시작한다. 1+1이기 때문에
    cnt.append(sum.count(i))

a=2 # 2가 제일 작은 수이기 때문에 a에 2를 저장해놓고
result=[] # 결과 값을 저장할 리스트도 선언한다. 
for i in cnt: # cnt 리스트를 돌리면서 
    if i==max(cnt): # i가 합이 나온 최댓값과 같다면 
        result.append(a) # result에 저장한다. 
    a+=1
print(*result) # 리스트 출력할 때, 대괄호 없이 한번에 출력하려면 *리스트 하면 된다.
