import random
x=raw_input("row number")
y=raw_input("line number")
fn=x+y+".txt"
f=open(fn,"w")
for i in range(int(x)):
	for j in range(int(y)):
		f.write(str(random.randint(-200,300)))
		if (j<int(y)-1):
			f.write(" ")
	f.write("\n")
f.close()
