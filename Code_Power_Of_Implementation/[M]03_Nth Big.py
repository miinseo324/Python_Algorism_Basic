N, K = map(int,input().split()) # N : 자연수 개수, K : k번째 큰 수 출력
N_list=list(map(int, input().split()))
N_list.sort(reverse=True)
print(N_list[K-1])
