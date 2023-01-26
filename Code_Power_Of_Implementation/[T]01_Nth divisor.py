import sys
sys.stdin=open("input.txt", "rt")
n, k =map(int, input().split())
# 숫자가 뛰어쓰기로 놓여져있으면 map 함수로 읽어야 한다.
# split()가 문자들을 분리해서 읽도록 해준다.

cnt=0
for i in range(1, n+1):
    if n%i==0:
        cnt +=1
    if cnt==k:
        print(i)
        break
else:
    # 중간에서 break 당하면 else를 하지 않지만,
    #정상적으로 for문이 끝난다면 else가 실행된다.
    print(-1)
