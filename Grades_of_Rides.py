a,b,c=map(int,input().split())
if(a>50 and b>60 and c>100):
    print(10)
elif(a>50 and b>60 and c<100):
    print(9) 
elif(b>60 and c>100 and a<50):
    print(8)  
elif(a>50 and c>100 and b<60):
    print(7) 
elif(a>50 and b<60 and c<100) or (b>60 and a>50 and c<100) or (c>100 and a<50 and b<60):
 print(6)
else:
 print(5)