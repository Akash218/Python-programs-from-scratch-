def cap(s):
    t=s.split(' ')
    for i in range(len(t)):
        a=t[i].capitalize()
        print(str(a),end=" ")
cap('changed form')