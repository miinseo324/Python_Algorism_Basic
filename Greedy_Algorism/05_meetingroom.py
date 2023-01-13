import sys
sys.stdin=open("input.txt", "r")
n=int(input())
meeting=[]
for i in range(n):
    s,e=map(int, input().split())
    meeting.append((s,e))
    # meeting 이라는 리스트에 튜플 형태로 입력
meeting.sort(key=lambda x : (x[1], x[0]))
# meeting에서 x[1]이 첫순위가 되고 x[0]이 두번째 순위가 되서 정렬하라.
et=0
#end time
cnt=0
for s, e in meeting:
    if s>=et:
        et=e
        cnt+=1
print(cnt)
