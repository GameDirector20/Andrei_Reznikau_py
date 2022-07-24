
# with open('c:/Users/81236312/Documents/GitHub/Andrei_Reznikau_py/Tasks/Task3/test-test.txt', 'r') as f:
    
#     print(f.read())
#     f.seek(0)
    
#     x = f.read(5)
#     print(x, f'position - {f.tell()}')

#     # f.seek(4)
#     x = f.read(5)
#     print(x, f'position - {f.tell()}')

    # f.seek(0)

    # for i in range(15):
    #     x = f.readline(3)
    #     print(x,  f'position - {f.tell()}')

    # else:
    #     x = '10'

    # print(x, len(x),  f'position - {f.tell()}')

    # xl = []

    # xl.append(x)
    # print(xl)

    # xl.append('x')

    # print(xl)

s = '0123456789\n'

s_w = '0123456789'

l = []

l.append(s)

l_w = []

l_w.append(s_w)

b = '\n' in s

bs = "\n" in s_w

print(f" leng of str with N - {len(s)}, {b}")

print(f' leng of str without N - {len(s_w)}, {bs}')

print(f' leng of lst with N - {len(l)}')

print(f' leng of lst without N - {len(l_w)}')