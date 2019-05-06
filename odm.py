n, m ,od= int(input()) ,int(input()) , []
num = str(n)
l = len(num)
od = []

for i in range(10**(l-1),10**l):
    if str(i) == "".join(sorted(str(i))) and  len(set(str(i))) == len(str(i)):
        od.append(i)
l2 = len(od)


def is_odo(k):
    for i in range(l2):
        if od[i] == k:return 1

def prev_num(i  , j):
    return od[(od.index(i))- j]

def next_num(i , j):
    if(od.index(i)-(od.index(i)+j))<0:
        return od[((od.index(i)+j)-(len(od)))]
    return od[(od.index(i)) + j]


if( is_odo(n)):
    P = prev_num(n,m)
    N = next_num(n,m)
    print(P , N)
    print("the previous reading",prev_num(n,1))
    print("the next reading",next_num(n,1))
    print("the difference between readings is",abs(od.index(P) - od.index(N)))
else:print("invalid")
