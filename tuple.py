#creating a tuple
my_tuple=(3,4.6,"Ashmi")
print(f'\n {my_tuple} \n')

#nested tuple
n_tuple=("mouse",[8,4,6],(1,2,3))
print(f' {n_tuple} \n')

#number of items in a tuple len
print(f'Number of items={len(n_tuple)}\n')

#retrieving items from tuple
print(f'2nd item in tuple={n_tuple[1]}\n')

#retrieving 4 from the list
print(f'to retrive 4 from list= {n_tuple[1][1]}\n')
print(f'retreiving s from mouse= {n_tuple[0][3]}\n')
print(f'retrieving 3= {n_tuple[2][2]}\n')

#retrieve use from mouse
print(f'retrieving use from mouse= {n_tuple[0][2:5]}\n')
tuple2=('p','r','o','g','r','a','m','i','z')
print(f'retrieving rog from tuple2 {tuple2[1:4]}\n')

#retrieve the element using negative index
print(f"retrieving 'p','r' from tuple2= {tuple2[0:-7]}\n")

tuple3=(4,2,3,[6,5])

#tring to change the item from a tuple
#it will give error it is immutable
#tuple3[1]=9
#print(f'{tuple3}\n')

#
stuDetails=('Ashmi',89)

#packing
adress=('227','pensylvania','mars','197')
for x in adress:
    print(x,end=' ')
