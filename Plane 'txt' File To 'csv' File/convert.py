f=open('input.txt','r')
f2=open('out.csv','w')
for line in f:
    l=line.split(" ")
    str=",".join(l)
    f2.write(str+'\n')
f.close()
f2.close()
