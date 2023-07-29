def do_bubble_sort(array):
    array_size = len(array)
    for index in range(array_size):
        is_need_to_swap_elements = False

        for j in range(0, array_size - index - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_need_to_swap_elements = True

        if not is_need_to_swap_elements:
            break

    return array


my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = do_bubble_sort(my_list)
print(sorted_list)
