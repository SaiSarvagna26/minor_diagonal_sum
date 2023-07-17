rows,columns=input().split()
rows,columns=int(rows),int(columns)
k=[]
sum1=0
for i in range(rows):
    list_a=list(map(int,input().split()))
    k.append(list_a)
for j in range(columns):
    first_row=k[j][columns-j-1]
    sum1=sum1+first_row
print(sum1)