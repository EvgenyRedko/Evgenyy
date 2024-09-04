my_dict = {'Evgeny': 1998, 'Oksana': 1998, 'Roma': 1992}
print(my_dict)
print(my_dict['Evgeny'])
print(my_dict.get('Alisa'))
my_dict.update({'Alisa': 1999,
                'Yliya': 1966})
print(my_dict)
b= my_dict.pop('Evgeny')
print(my_dict)
print(b)
print(my_dict)
my_set = {1,2,3,4,1,2,3,4, 'Ручка','Ручка','Ручка,','Ручка'}
print(my_set)
my_set.update([7,8,11,12,13])
my_set.remove(1)
print(my_set)
