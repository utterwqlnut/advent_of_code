import sys
sys.stdin = open("rpc2.in","r")
total=0
dict = {'A':0,'B':1,'C':2}
win = {'A':1,'B':2,'C':0}
lose = {'A':2,'B':0,'C':1}
while True:
    try:
        a,b = input().split()
        if b=='X':
            total+=lose[a]+1
        elif b=='Y':
            total+=dict[a]+4
        else:
            total+=win[a]+7
    except EOFError:
        break
print(total)
