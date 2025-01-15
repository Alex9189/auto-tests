my_list = [11, 28, 43, 64, 85]
a = 0
# for i in range(1, 4):
#     a += i
# print(a)
# # print(i)
# # # print(i+2)
# for i in enumerate(my_list):
#     print(i)
# for idx, value in enumerate(my_list):
#     print(idx, value)
#     my_list[idx] = value + 1
# print (my_list)
strange_phonebook = [
    ["Alex", "Andrew"],
    ["Barry", "Bill"],
    ["Casey","Cindy"],
    ["Danny", "Donovan"]]
for letter in strange_phonebook:
    for name in letter:
        for character in name:
            print(character, end=' ')