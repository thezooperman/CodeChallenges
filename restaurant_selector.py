r1 = ['a','b']
r2 = ['b', 'c','a','d']

combined_index = None
last_restaurant = ''
for index, r in enumerate(r1):
    if r in r2:
        index_of_r1 = index
        index_of_r2 = r2.index(r)
        temp_index = index_of_r1 + index_of_r2
        if combined_index is None:
            combined_index = temp_index
            last_restaurant = r
        else:
            combined_index = min(temp_index, combined_index)
            last_restaurant = r
if combined_index is None:
    print('YELP')
else:
    print(last_restaurant)
