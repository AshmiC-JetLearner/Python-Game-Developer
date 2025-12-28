friend_list=['Olivia','Addy','Halyn','Sophia','Olivia']
print(f'Friend list={friend_list}\n')
print(f' Data type of items={type(friend_list)}\n')

#total number of items
print(f' Data type of items={type(friend_list)}\n')

#How many times Olivia occurs in the list
print(f' Number of times Oliva occurs={friend_list.count('Olivia')}\n')

#adding an item at the end of the list
friend_list.append('Kelsey')
print(f'Friend list={friend_list}\n')

#creating 2nd list
Hobby_list=["soccer",'drawing','taekwondo','sewing','crafting']
friend_list.extend(Hobby_list)
print(f'Friend list={friend_list}\n')

# 2 ways to delete an item from a list

# first way delete an item by it's name
friend_list.remove('drawing')
print(f'Friend list={friend_list}\n')

# second way to delete an item by using index
friend_list.pop(-1)
print(f'Friend list={friend_list}\n')

#iterating list items
tot_items=len(friend_list)
print(f' Total items in list={tot_items}\n')

for i in range (len(friend_list)):
    print(f'item at index {i}={friend_list[i]}')


#finding index numbers for a particular item
print(f'\nfriend_list.index("Olivia")')

#searching an item by using "in" and 'not in' keywords
print('drawing' in friend_list)
print('drawing' not in friend_list)
