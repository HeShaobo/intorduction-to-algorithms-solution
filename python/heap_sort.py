# encoding=utf8

import utils
from pprint import pprint


def max_heapify(array, size, index):
    """维护节点i的最大堆
    """
    l = index*2 + 1
    r = index*2 + 2
    max = index
    if l < size and array[l] > array[index]:
        max = l
    if r < size and array[r] > array[max]:
        max = r
    if max != index:
        array[index], array[max] = array[max], array[index]
        max_heapify(array, size, max)

def init_heapify(array):
    """建堆"""
    size = len(array)
    for i in range(size/2-1, -1, -1):
        max_heapify(array, size, i)

def heap_sort(array):
    size = len(array)
    init_heapify(array)
    for i in range(size-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        size -= 1
        max_heapify(array, size, 0)
    return array


if __name__ == '__main__':
    array = utils.get_random_int_array()
    print 'init array:'
    pprint(array)
    print 'heap sort result'
    pprint(heap_sort(array))
