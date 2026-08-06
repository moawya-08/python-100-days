import random

rock='''       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"'''


scissor='''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/'''

paper='''   _.-._
                    | | | |_
                    | | | | |
                    | | | | |
                  _ |  '-._ |
                  \`\`-.'-._;
                   \    '   |
                    \  .`  /
                     |    |
'''

computer=(random.randint(0,2))

choice=int(input("What do you choose?\n Type 0 for Rock, 1 for paper, 2 for scissor\n"))
if choice== 0:
    print(rock)
elif choice== 1:
    print(paper)
elif choice== 2:
    print(scissor)
else:
     print("Wrong choice")


print("\nComputer chose: \n")
if computer == 0:
  print(rock)
elif computer ==1:
   print(paper)
elif computer ==2:
  print(scissor)



if choice == computer:
   print("Draw")
elif choice ==0 and computer == 1:
  print("you lose")
elif choice == 0 and computer == 2:
   print("you win")
elif choice ==1 and computer == 0:
     print("you win")
elif choice == 1 and computer == 2:
     print("You lose")
elif choice == 2 and computer == 0:
     print("You lose")
elif choice == 2 and computer == 1:
    print("You win")
else:
    print("   ")
