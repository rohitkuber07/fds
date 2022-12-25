row = int(input("Enter the row count :"))
col = int(input("Enter the coloum count:"))

m1=[[0 for i in range(col)] for i in range(row)]
m2=[[0 for i in range(col)] for i in range(row)]
ans = [[0 for i in range(col)] for i in range(row)]

print("enter the data foe=r matrix1:")
for i in range(row):
    for j in range(col):
        m1[i][j]= int(input(f" Enter the value for row{i+1} and col{j+1}:"))

print("Enter the data for matrix2:")
for i in range(row):
    for j in range(col):
        m2[i][j]=int(input(f" Enter the val for row{i+1} and col {j+1}:"))

#m1=[[2,3],[4,5]]
#m2=[[2,3],[8,9]]
#ans=[[0,0],[0,0]]
#row=2
#col=2

#addition
for i in range(row):
    for j in range(col):
        ans[i][j]=m1[i][j]+m2[i][j]

print(ans)

#substraction
for i in range(row):
    for j in range(col):
        ans[i][j]=m1[i][j]-[i][j]
print(ans)

#transpose
ans=[[0 for i in range(row)] for j in range(col)]
for i in range(row):
    for j in range(col):
        ans[i][j] = m1[i][j]
print("4.transpose:",ans)

#multiplication
if(len(m1[0])==len(m2)):
    print("Multiplication possible")
ans=[[0 for i in range(len(m2[0]))] for j in range(len(m1))]

for i in range(row):
    for j in range(col):
        for k in range(row):
            ans[i][j] += m1[j][k]*m2[k][j]

else:
    print("Multiplication Not possible")
print("Multiplication:",ans)