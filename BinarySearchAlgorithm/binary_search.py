

def binary_search(list, key):
    mid = 0
    start = 0
    end = len(list)
    steps = 0

    while start <= end:
        print("Step", steps, ":", str(list[start:end+1]))

        steps = steps+1
        mid = (start + end) // 2

        if key == list[mid]:
            return mid
        if key < list[mid]:
            end = mid-1
        else:
            start = mid+1

    return -1


my_list = input('Enter Your search List, Separate By (,): ')
search_list = [int(x) for x in my_list.split(',')]
target = input('Enter Search Target: ')


binary_search(search_list , int(target))

if target in search_list :
    print("Successful Search!")
    print('Number found in index: ', search_list .index(target))
else:
    print("Unsuccessful Search")
