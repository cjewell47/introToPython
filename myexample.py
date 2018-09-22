print('hello world')
my_income = 1000
my_taxrate = 0.2
my_taxes = (my_income - 100) * my_taxrate
print(my_taxes)
a = 'abcdefghij'
print(a[0:3])
print(a[::2])
print(a[1::2])
print(a[::-1])
print('My name is {a} {b} {c}'.format(a='Don', b='Chucho', c='Salamanca'))
print('My initials are {b}{c}'.format(a='Don', b='Chucho'[0], c='Salamanca'[0]))
r = 100/7
s = '14'
print('100 divided by 7 is {a:1.4f}'.format(a=r))
# print(f'100 divided by 7 is about {r}') 3.6? f string works in notebook, not on my machine though
my_list = [1,2,3,4,5]
another_list = [6,7,8,9,10]
new_list = my_list + another_list
new_list.append(11)
new_list.pop()
print(new_list)
