def swap_case(s):
    c=''
    for i in s:
        if i==i.lower():
            a=i.upper()
        else:
            a=i.lower()
        c=c+a
    return c
print(swap_case(input()))





