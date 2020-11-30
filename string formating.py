def print_formatted(number):
    width = len('{:b}'.format(number))
    for i in range(1,number+1):
        print(str.rjust(str(i),width),str.rjust(str(oct(i)[2:]),width),str.rjust(str(hex(i).upper()[2:]),width),str.rjust(str(bin(i)[2:]),width))
if __name__ == '__main__':
    n= int(input())
print_formatted(n)