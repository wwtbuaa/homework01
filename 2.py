x=raw_input("row number\n")
y=raw_input("line number\n")
f=open(x+y+".txt","r")
num=[]
for i in range(int(x)):
    for j in range(int(y)):
        l=f.readline()
        l=l.strip('\n').split(" ")
        num.append(l)
def maxsum(num,y1,x1):
    temp=[0]*x1
    s=0
    a=-1000000
    for i in range(y1):
        for j in range(i,y1):
            for k in range(x1):
                temp[k]+=int(num[j][k])
                if(s+temp[k]<temp[k]):
                    s=0
                s+=temp[k]
                if(a<s):
                    a=s
            s=0
        s=0
        temp=[0]*x1
    return a
print maxsum(num,int(x),int(y))
        
