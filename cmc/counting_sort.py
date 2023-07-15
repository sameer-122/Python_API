import sys


def counting_sort(l:list) :
    mx = -sys.maxsize
    mn = sys.maxsize
    for x in l: mx = max(mx,x)
    for x in l: mn = min(mn,x)
    print(mn,mx)

    count = [0]*(mx-mn+1)
    for x in l:
        count[x-mn]+=1
    l = []
    for i in range(len(count)):
        while count[i]:
            l.append(mn+i)
            count[i]-=1
    return l


if __name__ == '__main__':
    l = [x for x in range(1100, 1000, -1)]
    l[1]= 1002
    print(l)
    l = counting_sort(l)
    print(l)