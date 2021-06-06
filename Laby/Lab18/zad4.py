from heapq import heappush, heappop
import timeit


def heapsort(a):
    heap = []
    for i in a:
        heappush(heap, i)
    size = len(heap)
    return [heappop(heap) for i in range(size)]


x = '''
def heapsort(a):
    heap = []
    for i in a:
        heappush(heap, i)
    size = len(heap)
    return [heappop(heap) for i in range(size)]
'''


def partition(array, begin, end):
    pivot = begin
    for i in range(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quick_sort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quick_sort(array, begin, pivot - 1)
        _quick_sort(array, pivot + 1, end)

    return _quick_sort(array, begin, end)


y = '''
def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quick_sort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quick_sort(array, begin, pivot-1)
        _quick_sort(array, pivot+1, end)
    return _quick_sort(array, begin, end)
'''''

a = [9, 2, 3, 0, 13, 14, 11, 10, 3]

print(heapsort(a))

a1 = [9, 2, 3, 0, 13, 14, 11, 10, 3]

quick_sort(a1, 0, len(a1) - 1)
print(a1)

x_res = timeit.timeit(stmt=x)
y_res = timeit.timeit(stmt=y)
print(x_res)
print(y_res)

with open('res.txt', 'w') as f:
    f.writelines(f'x = {str(x_res)}   ')
    f.writelines(f'y = {str(y_res)}')