
def Insertion_Sort(numbers_list):
    for i in range(1, len(numbers_list)):
        j = i
        while j != 0:
            if int(numbers_list[j]) < int(numbers_list[j - 1]):
                numbers_list[j], numbers_list[j - 1] = numbers_list[j - 1], numbers_list[j]
                j -= 1
            else:
                break
    return numbers_list
 
list = Insertion_Sort(input('Entre your numbers: ').split())

for i in list:
    print(int(i), sep='', end=' ')
