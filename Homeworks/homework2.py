#Beyza Özgür

import collections

name_list = ["Beyza Özgür", "Jack London", "Oscar Wilde", "Jessica Jones", "Harleen Quinzel"]
grade_list = [[70, 80, 90], [50, 55, 60], [98, 99, 100], [95, 96, 97], [10, 20, 30]]

average_list = []

sum = 0
average = 1

for i in range(5):
    for j in range(3):
        sum += grade_list[i][j]
        j += 1
    average = sum / 3
    average_list.append(average)
    sum = 0
    i += 1

info = {name_list[0]: average_list[0], name_list[1]: average_list[1], name_list[2]: average_list[2],
        name_list[3]: average_list[3], name_list[4]: average_list[4]}

sorted_avg = sorted(info.items(), key=lambda key_val: key_val[1])
sorted_dict = collections.OrderedDict(sorted_avg)

max = next(iter(info.values()))

keys = list(info.keys())
values = list(info.values())

for i in info.values():
    if i > max:
        max = i
        print("Congratulations {}! You have the highest grade!".format(keys[values.index(max)]))

print("Maximum grade = ", max)
print(sorted_dict)