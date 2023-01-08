import random

# Constants for card suits and ranks
SUITS = ['H', 'D', 'C', 'S']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Create a deck of cards
deck = [rank + suit for rank in RANKS for suit in SUITS]

# Shuffle the deck
random.shuffle(deck)

# Initialize player's and dealer's hands
player_hand = []
dealer_hand = []

# Deal initial cards to player and dealer
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

# Calculate the sum of a hand of cards
def calculate_hand(hand):
  sum = 0
  num_aces = 0
  for card in hand:
    rank = card[0]
    if rank == 'A':
      sum += 11
      num_aces += 1
    elif rank in ['J', 'Q', 'K']:
      sum += 10
    else:
      sum += int(rank)
  
  # Handle the case where the hand has one or more aces and the sum is over 21
  while sum > 21 and num_aces > 0:
    sum -= 10
    num_aces -= 1

  return sum

# Print the player's and dealer's hands
def print_hands():
  print("Player's hand:", *player_hand, sep=' ')
  print("Dealer's hand:", *dealer_hand, sep=' ')

# Prompt the player to hit or stand
def player_turn():
  global player_hand
  while True:
    action = input("Hit or stand (H/S): ")
    if action.upper() == 'H':
      player_hand.append(deck.pop())
      print_hands()
      if calculate_hand(player_hand) > 21:
        print("You bust!")
        return
    elif action.upper() == 'S':
      return

# Dealer's turn
def dealer_turn():
  global dealer_hand
  while calculate_hand(dealer_hand) < 17:
    dealer_hand.append(deck.pop())
  print_hands()
  if calculate_hand(dealer_hand) > 21:
    print("Dealer busts!")

# Play the game
print_hands()
player_turn()
dealer_turn()

# Determine the winner
player_sum = calculate_hand(player_hand)
dealer_sum = calculate_hand(dealer_hand)
if player_sum > dealer_sum:
  print("You win!")
elif player_sum == dealer_sum:
  print("It's a tie!")
else:
  print("You lose!")