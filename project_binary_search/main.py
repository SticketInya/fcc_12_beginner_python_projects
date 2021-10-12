import random
from search import binary_search


if __name__ == '__main__':
    random_list = []
    for i in range(100):
        random_list.append(random.randint(0,1000))
    sorted_list =sorted(random_list)
    search_target = random.randint(0,99)
 
    print(f"The target index is {search_target}")
    result = binary_search( sorted_list, sorted_list[search_target])
    print(f'The result of the search is {result}')