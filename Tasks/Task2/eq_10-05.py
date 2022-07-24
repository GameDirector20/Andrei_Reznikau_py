eq_val = input("Please, enter your equation:")

x = input("please, enter the value of x:")

# y = kx +/- b

c = eq_val.replace(' ', '').replace('y=','').split('x')

res = int(c[0]) * int(x) + int(c[1])

print(res, type(res))