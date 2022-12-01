import sys
# Uses file io
def main():
    sys.stdin = open("calories.in", "r")
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
    print(max(calories))
if __name__=='__main__':
    main()
