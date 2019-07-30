# python3
import time
import random

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_opti1(numbers):
    n = len(numbers)
    sorted_list = sorted(numbers)
    return sorted_list[-1] * sorted_list[-2]

def max_pairwise_product_opti2(numbers):
    n = len(numbers)
    max_num1 = -1
    max_index1 = 0
    for i in range(n):
        if (numbers[i] > max_num1 or i == 0):
            max_num1 = numbers[i]
            max_index1 = i
    max_num2 = -1
    max_index2 = 0           
    for i in range(n):
        if ((numbers[i] > max_num2 or i == 0) and (i != max_index1 )):
            max_num2 = numbers[i]
            max_index2 = i    
    return max_num1 * max_num2




if __name__ == '__main__':
    #input_n = int(input())
    #input_numbers = [int(x) for x in input().split()]
    input_n = 100
    input_numbers = [random.randint(0, 1000) for x in range(input_n)]
    print(input_numbers)
    start = time.time()
    print(max_pairwise_product(input_numbers))
    print(time.time() - start)
    start = time.time()
    print(max_pairwise_product_opti1(input_numbers))
    print(time.time() - start)    
    start = time.time()
    print(max_pairwise_product_opti2(input_numbers))
    print(time.time() - start) 