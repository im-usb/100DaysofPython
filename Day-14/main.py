from art import logo
from art import vs
from game_data import data
import random
import replit


def random_data():
  profile_detail = random.choice(data)
  return profile_detail

def compare(player_choice):
  if player_choice =='a' and pick_1['follower_count'] > pick_2['follower_count']:
    return True
  elif player_choice =='b' and pick_1['follower_count'] < pick_2['follower_count']:
    return True
  else:
    return False


print(logo)
print("Welcome!!")
player_win = True
player_score = 0
player_choice = 'a'
  
while player_win == True:
  pick_1 = random_data()
  pick_2 = random_data()
  print(f"Compare A: {pick_1['name']}, {pick_1['description']} from {pick_1['country']}")
  print(vs)
  print(f"Against B: {pick_2['name']}, {pick_2['description']} from {pick_2['country']}")
  player_choice = input("Who has more Followers? A or B: ").lower()
  
  player_win = compare(player_choice)

  if player_win == True:
    player_score +=1
  
  replit.clear()
  print(logo)
  print(f"Your Score: {player_score}")

print("thanks")
      
    
  

