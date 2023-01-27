N=int(input())
# N에다가 학생 수
s_score=list(map(int,input().split()))
# s_score에 학생 수만큼 입력한다.
avg=round(sum(s_score)/N)
# 소수 첫째 자리에서 반올림하는 법 배우기
s_abs=[] # (N명의 학생들의 점수-평균)의 절댓값을 담을 리스트
for i in s_score: #학생들의 점수 리스트를 돌린다.
    s_abs.append(abs(i-avg)) # (N명의 학생들의 점수-평균)의 절댓값을 추가한다.
min_abs=[] # 최소 절대값들의 인덱스를 담을 리스트를 선언한다.
for i in s_abs: # (N명의 학생들의 점수-평균)의 절댓값을 돌린다. N명의 학생들꺼.
    if min(s_abs)==i: # 절대값들 중 최소값과 비교한다 하나씩
        abs_ind=s_abs.index(i) # 최소 절대값의 인덱스 
        min_abs.append(s_abs.index(i)) # 최소 절대값 리스트에 해당 인덱스를 추가한다.
        s_abs[abs_ind]=max(s_abs) # 리스트에 같은 값들이 여러개 있어도 제일 첫번째 인덱스만 출력하니까.
        #인덱스를 저장하고 나면 다음 인덱스를 저장하기 위해 저장한 인덱스에는 다른 값을 넣어놓는다.
if len(min_abs)==1: # 만약 최소 절대값의 개수가 한개면, 그냥 출력한다. 
    print(avg, min_abs+1)
else:
    result=0 # 하나가 아니라면, 일단 result 변수에 0을 저장하고 
    for i in min_abs:# 최소 절대값 인덱스를 돌린다. 
        if result<s_score[i]: # 해당 인덱스의 실제값이 원래보다 크다면 result에 저장한다.
            result=s_score[i] # 결국 result에는 최소 절대값중에서 가장 큰 수가 저장되고
    print(avg, s_score.index(result)+1) # 인덱스를 돌리면, 제일 처음의 순서 인덱스가 나온다.
        
