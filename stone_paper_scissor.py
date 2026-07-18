import random
choices=['stone','paper','scissor']
play='yes'
while play=='yes':
    user=input('enter your choice:').lower()
    computer=random.choice(choices)
    if user==computer:
        print(' Tie  ')
    elif(user=='stone' and computer=='scissor') or \
        (user=='paper' and computer=='stone') or \
        (user=='scissor' and computer=='paper'):
        print('You Won !')
    elif user in choices:
        print('Computer won')
    else:
        print('Invalid choice')
    play=input('Do you want to continue this game (yes/no)??').lower()
print('Thanks for playing!')
