list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]

for x, y, z in zip(list1, list2, list3):
    print(f"x: {x}, y: {y}, z: {z}")