"""Binar search for sorted list"""
n=list(map(int,input("enter elements:").split( )))
k=int(input("enter key element:"))
l=0
h=len(n)-1
f=0
while(l<=h):
    m=(l+h)//2
    if(n[m]<k):
        l=m+1
    if(n[m]>k):
        h=m-1
    if(n[m]==k):
        print(m+1)
        f=1
        break
if(f==0):
    print(-1)
