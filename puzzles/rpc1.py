import sys
def winLoseDraw(p2,p1):
    if p2==p1:
        return 0
    elif p2==0 and p1==2:
        return 1
    elif p2==0 and p1==1:
        return 2
    elif p2==1 and p1==0:
        return 1
    elif p2==1 and p1==2:
        return 2
    elif p2==2 and p1==0:
        return 2
    else:
        return 1
sys.stdin = open("rpc1.in","r")
total=0
dict1 = {'X':0,'Y':1,'Z':2}
dict2 = {'A':0,'B':1,'C':2}
while True:
    try:
        a,b = input().split()
        p2 = dict1[b]
        p1 = dict2[a]
        result = winLoseDraw(p2,p1)
        if result==0:
            total+=4+p2
        elif result==1:
            total+=7+p2
        else:
            total+=p2+1
    except EOFError:
        break
print(total)
