sequence_of_numbers = input("Введите любые числа через пробел:")
user_number = int(input("Введите любое число:"))
numbers = list(map(int, sequence_of_numbers.split()))

numbers.append(user_number)
print(numbers)


def sort(num):
    for run in range(len(num)-1):
        for every in range(len(num)-1-run):
            if num[every] > num[every + 1]:
                num[every], num[every + 1] = num[every + 1], num[every]
    return num


print("Отсортированный список в порядке возрастания:", sort(numbers))

sorted_sequence_of_numbers = sort(numbers)


def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:
       return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


index_user_number = binary_search(sorted_sequence_of_numbers, user_number, 0, len(sorted_sequence_of_numbers)-1)


print("Индекс элемента введенного пользователем:", index_user_number)
if index_user_number == 0:
    print("Меньше индекса не существует.")
else:
    previous_index = index_user_number - 1
    print("Индекс предыдущего элемента:", previous_index)


if len(sorted_sequence_of_numbers)-1 == index_user_number:
    print("Больше индекса не существует.")
else:
    next_index = index_user_number + 1
    print("Индекс следующего элемента:", next_index)


