# def insertion_sort(list):
#     l = list
#     for i in range(1,len(list),1):
#
#         if l[i] < l[i-1]:
#             for j in range(i,0,-1):
#                 if l[j] >l[j-1]: break
#                 l[j], l[j-1] = l[j-1], l[j]
#     return l
#
def insertion_sort(list):
    l = list
    for i in range(1,len(list),1):
        j=i
        while l[j]<l[j-1] and j>0:
            l[j], l[j-1] = l[j-1], l[j]
            j-=1
    return l

if __name__ == '__main__':
    l = [52,33,14,6,2,1,44,23,65,73,53]
    print(l)
    k= insertion_sort(l)
    print(l)