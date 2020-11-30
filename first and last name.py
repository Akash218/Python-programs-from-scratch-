'''def print_full_name(a, b):
    print("Hello",a,b+"!"," You just delved into python.")
if __name__ == '__main__':
    x=input()
    y=input()
    print_full_name(x,y)'''

'''def mutate_string(string, position, character):
    a=list(string)
    a[position]=character
    string=''.join(a)
    return string'''

'''def count_substring(string, sub_string):
    count=0
    x=0
    a=list(string)
    b=list(sub_string)
    c=len(b)
    for i in range(0,len(a)):
        if a[int(i):int(c)]==b:
            count=count+1
            c=c+1
        else:
            count=count
            c=c+1
    return count
print(count_substring('I am an Indian, by birth.','Birth'))'''


#method 1
a=input()
print(any(map(str.isalnum,a)))
print(any(map(str.isalpha,a)))
print(any(map(str.isdigit,a)))
print(any(map(str.islower,a)))
print(any(map(str.isupper,a)))

#method 2
print(any(char.isalnum for char in a))
print(any(char.isalpha for char in a))
print(any(char.isdigit for char in a))
print(any(char.islower for char in a))
print(any(char.isupper for char in a))
