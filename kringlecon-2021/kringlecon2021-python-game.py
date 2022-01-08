### level 0

import elf, munchkins, levers, lollipops, yeeters, pits
# Grab our lever object
lever = levers.get(0)
munchkin = munchkins.get(0)
lollipop = lollipops.get(0)
# move to lever position
elf.moveTo(lever.position)
# get lever int and add 2 and submit val
answer = lever.data() + 2
lever.pull(answer)
# Grab lollipop and stand next to munchkin
elf.moveLeft(1)
elf.moveUp(8)
# Solve the munchkin's challenge
munchList = munchkin.ask() # e.g. [1, 3, "a", "b", 4]
answer_list = []
for elem in munchList:
    if type(elem) == int:
        answer_list.append(elem)
munchkin.answer(answer_list)
elf.moveUp(2) # Move to finish

### level 1

import elf, munchkins, levers, lollipops, yeeters, pits
lollipop = lollipops.get(0)
elf.moveTo(lollipop.position)
elf.moveUp(10)

### level 2

import elf, munchkins, levers, lollipops, yeeters, pits
all_lollipops = lollipops.get()
lollipop1 = all_lollipops[1]
elf.moveTo(lollipop1.position)
elf.moveRight(3)
elf.moveUp(2)
elf.moveTo({'x':2, 'y':2})

### level 3

import elf, munchkins, levers, lollipops, yeeters, pits
lever0 = levers.get(0)
lollipop0 = lollipops.get(0)
elf.moveLeft(6)
ans = int(lever0.data()) + 2
lever0.pull(ans)
elf.moveTo(lollipop0.position)
elf.moveTo({'x':2, 'y':2})

### level 4

import elf, munchkins, levers, lollipops, yeeters, pits
# Complete the code below:
lever0, lever1, lever2, lever3, lever4 = levers.get()
# Move onto lever4
elf.moveLeft(2)
# This lever wants a str object:
lever4.pull("A String")
# Need more code below:
elf.moveTo(lever3.position)
lever3.pull(True)
elf.moveTo(lever2.position)
lever2.pull(1)
elf.moveTo(lever1.position)
lever1.pull(['amirootyet'])
elf.moveTo(lever0.position)
lever0.pull({'amirootyet': 'amirootyet'})
elf.moveTo({'x':2, 'y':2})

### level 5

import elf, munchkins, levers, lollipops, yeeters, pits
lever0, lever1, lever2, lever3, lever4 = levers.get()
elf.moveTo(lever4.position)
lever4ans = (str(lever4.data()) + " concatenate")
lever4.pull(lever4ans)

elf.moveTo(lever3.position)
lever3ans = not (lever3.data())
lever3.pull(lever3ans)

elf.moveTo(lever2.position)
lever2ans = 1 + lever2.data()
lever2.pull(lever2ans)
elf.moveTo(lever1.position)
lever1lst = lever1.data()
lever1lst.append(int(1))
lever1.pull(lever1lst)
elf.moveTo(lever0.position)
lever0dict = lever0.data()
lever0dict.update({"strkey":"strvalue"})
lever0.pull(lever0dict)
elf.moveTo({'x':2, 'y':2})

### level 6

import elf, munchkins, levers, lollipops, yeeters, pits

lever = levers.get(0)
elf.moveTo(lever.position)
data = lever.data()
if type(data) == bool:
    data = not data
elif type(data) == int:
    data = data * 2 
elif type(data) == list:
    data = [x+1 for x in data]
elif type(data) == str:
    data = data+data
elif type(data) == dict:
    data['a'] = data.get('a', 0) + 1
else:
    print(data)

lever.pull(data)
elf.moveTo({'x':2, 'y':2})

### level 7

import elf, munchkins, levers, lollipops, yeeters, pits
for num in range(6): #not sure if number is right
    elf.moveLeft(3)
    elf.moveUp(31337)
    elf.moveLeft(2)
    elf.moveDown(31337)

### level 8

import elf, munchkins, levers, lollipops, yeeters, pits
all_lollipops = lollipops.get()
for lollipop in all_lollipops:
    elf.moveTo(lollipop.position)
lever = levers.get(0)
elf.moveTo(lever.position)
data = lever.data()
data.insert(0,"munchkins rule")
lever.pull(data)
elf.moveDown(31337)
elf.moveLeft(6)
elf.moveTo({'x':2, 'y':2})

