f=open('desktop/in.txt','r')
f1=open('desktop/out.txt','w')
a=['zero','one','two','three','four','five','six','seven','eight','nine','ten']
for line in f:
    res=''
    for i in line:
        if i != '\n': 
            res+=a[int(i)]+" "
        else:
            pass    
    f1.write(res+'\n')
    
f.close()
f1.close()