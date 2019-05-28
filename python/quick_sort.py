# encoding=utf-8

from utils import get_random_int_array

def partition(array, p, r):
    """数组划分"""
    # 选择最后一个元素作为主元
    x = array[r]
    i = p
    for j in range(p, r):
        if array[j] <= x:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[r], array[i] = array[i], array[r]
    return i

def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q-1)
        quick_sort(array, q+1, r)

if __name__ == '__main__':
    array = get_random_int_array(2000, 0, 100)
    print array
    # print partition(array, 0, len(array)-1)
    quick_sort(array, 0, len(array)-1)
    print array
