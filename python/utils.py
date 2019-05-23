# encoding=utf-8

import random

def get_random_int_array(length=8, min=1, max=100):
    """生成一个随机乱序的非负整形数组"""
    return [random.randint(min, max) for x in xrange(length)]


if __name__ == "__main__":
    print get_random_int_array(100)
