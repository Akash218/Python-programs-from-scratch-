n=int(input())
list=[]
for i in range(0,n):
    a=input().split()
    if a[0]=='insert':
        list.insert(int(a[1]),int(a[2]))
    elif a[0]=='append':
        list.append(int(a[1]))
    elif a[0]=='remove':
        list.remove(int(a[1]))
    elif a[0]=='pop':
        list.pop()
    elif a[0]=='sort':
        list.sort()
    elif a[0]=='reverse':
        list.sort(reverse=True)
    elif a[0]=='print':
        print(list)
    else:
        break


