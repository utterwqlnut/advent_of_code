import sys
sys.stdin = open("calories.in", "r")
def main():
    calories=[0]
    while True:
        try:
            calorie = input()
            if calorie=="":
                calories.append(0)
            else:
                calories[len(calories)-1]+=int(calorie);
        except EOFError:
            break
    calories.sort()
    print(calories[len(calories)-1]+calories[len(calories)-2]+calories[len(calories)-3])
if __name__=='__main__':
    main()
