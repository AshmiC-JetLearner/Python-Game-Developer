friends=(('Olivia',4121235677),('Addy',7248974320),('Evelyn',4123879234))
print(f'\n{friends}\n')

# Number of items
print(f'Number of items= {len(friends)}\n')

#getting an item from tuple
print(f'Olivia contact and number= {friends[0]}\n')

#getting a just the number
print(f"Addy's number= {friends[1][1]}\n")

#getting 412 from Evelyn number
#not working
#print(f'First 3 number of Evelyns number= {friends[2][1][0:3]}\n')

#use negative index
print(f"Olivia's number= {friends[0][-1]}\n")
