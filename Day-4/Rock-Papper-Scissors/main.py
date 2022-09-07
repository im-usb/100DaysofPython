import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

usr_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors."))
comp_choice = random.randint(0,2)
rps_list = [rock, paper, scissors]

if(usr_choice == 0 and comp_choice == 1):
    print(f"You chose \n {rps_list[usr_choice]}")
    print(f"Computer chose \n {rps_list[comp_choice]}")
    print("You lose")

elif(usr_choice == 0 and comp_choice == 2):
    print(f"You chose \n {rps_list[usr_choice]}")
    print(f"Computer chose \n {rps_list[comp_choice]}")
    print("You win")

elif(usr_choice == 1 and comp_choice == 0):
    print(f"You chose \n {rps_list[usr_choice]}")
    print(f"Computer chose \n {rps_list[comp_choice]}")
    print("You win")

elif(usr_choice == 1 and comp_choice == 2):
    print(f"You chose \n {rps_list[usr_choice]}")
    print(f"Computer chose \n {rps_list[comp_choice]}")
    print("You lose")

elif(usr_choice == 2 and comp_choice == 0):
    print(f"You chose \n {rps_list[usr_choice]}")
    print(f"Computer chose \n {rps_list[comp_choice]}")
    print("You lose")

elif(usr_choice == 2 and comp_choice == 1):
    print(f"You chose \n {rps_list[usr_choice]}")
    print(f"Computer chose \n {rps_list[comp_choice]}")
    print("You win")

elif(usr_choice == comp_choice ):
    print(f"You chose \n {rps_list[usr_choice]}")
    print(f"Computer chose \n {rps_list[comp_choice]}")
    print("It's a tie")

elif(usr_choice > 2 or comp_choice > 2 or usr_choice < 0 or comp_choice < 0):
  print("Game Over! Please enter the right choice and try again.")