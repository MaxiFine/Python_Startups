steps = 7

# for m in range(base):
#     for n in range(m+1):
#         print('*', end='')
#     print()


for x in range(1, steps, 2):
    for y in range(steps, x):
        print('#', end='')
    print()