#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) != 2:
        print('Paramater Error')
        exit()
    try:
        income=int(sys.argv[1])
    except ValueError:
        print("Parameter Error")
        exit()

    value=income-3500
    if value <=0:
        result = 0
    elif 0 < value <=1500:
        result = value * 0.03 - 0
    elif 1500 < value <=4500:
        result = value * 0.1 - 105
    elif 4500 < value <=9500:
        result = value * 0.2 - 555 
    elif 9500 < value <=35000:
        result = value * 0.25 - 1005
    elif 35000 < value <=55000:
        result = value * 0.3 - 2755
    elif 55000 < value <=80000:
        result = value * 0.35 - 5505
    else:
        result = value * 0.45 -13505
    print('{:.2f}'.format(result))

if __name__ == '__main__':
    main()