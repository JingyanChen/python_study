#sort arg
#lamada表达式，定义了一个匿名的函数，为他取名为comp，作用是比较x和y的大小 x<y是否为真
#定义了一个函数，函数名为select_sort 参数为可变的，一个或两个，第一个是输入数组，第二个是比较两个数大小的函数指针，默认给出了default值，是一个lambda函数
def select_sort(origin_items,comp=lambda x, y: x < y):
    """ simple select sort"""
    items = origin_items[:] #把输入参数赋值给局部变量items
    for i in range(len(items) - 1):
        min_index = i 
        for j in range(i+1,len(items)):
            if comp(items[j],items[min_index]):
                min_index = j
        items[i],items[min_index] = items[min_index],items[i]

    return items
def bubble_sort(origin_items, comp=lambda x, y: x > y):
    """bubble sort"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items
def merge_sort(items, comp=lambda x, y: x <= y):
    """归并排序(分治法)"""
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge(items1, items2, comp):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items

def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1
def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    da = [1,5,2,5,2,31,2,5,53,12,32]
    da1 = [1,9,2,6,3,5,2,4,6,2,3,6,88]
    da2 = [5,3,1,5,8,5,6,34,5,74,33,45]
    #print(merge_sort(da))
    print(merge(da1,da2,lambda x,y: x>y))
#chenjinyan is cool boy 才怪
"""cjy l love u"""
