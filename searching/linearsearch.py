n=list(map(int,input("Enter elements:").split( )))
k=int(input("enter key to search:"))
b=0
for i in range(len(n)):
    if(k==[i]):
        b=1
        c=i+1
        break
if(b==1):
    print("at index {0},{1} key element is present".format(c,k))
else:
    print(-1)

