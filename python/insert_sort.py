# encoding=utf8

import utils
from pprint import pprint


def insert_sort(array):
    if len(array) < 2:
        return array
    for i in xrange(1, len(array)):
        j = i
        value = array[i]
        while j > 0:
            if value < array[j-1]:
                array[j] = array[j-1]
                j -= 1
            else:
                break
        array[j] = value
    return array


if __name__ == '__main__':
    array = utils.get_random_int_array(1000, 1, 1000)
    print 'init array:'
    pprint(array)
    print 'sort result'
    pprint(insert_sort(array))
