Test_Case=int(input()) # 테스트 케이스 입력 받음
result=[]
for i in range(Test_Case):
    # 테스트 케이스만큼 반복한다.
    N, s, e, k=map(int, input().split())
    # N : N개의 자연수를 입력받는다.
    # 입력 받은 자연수를 s번째부터 e번째까지 자르고 오름차순으로 정렬한다.
    # k번째로 나타나는 숫자를 출력하라.
    N_list=list(map(int, input().split()))
    # N개의 자연수의 리스트를 만든다.
    a=N_list[s-1:e-1]
    a.sort()
    result.append(a[k-1])

for i in result:
    print("#{0} {1}".format(result.index(i)+1, i))
