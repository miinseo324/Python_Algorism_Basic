N=int(input())
num_list=list(input().split())
sum_list=[]
for i in num_list:
    a=map(int, list(i))
    sum_list.append(sum(a))
    
ind=sum_list.index(max(sum_list))
print(int(num_list[ind]))

