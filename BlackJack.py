from Deck import Card
import random

def deck_builder ():
    new_deck = []
    for suit in ('Club', "Heart", 'Spade', 'Diamond'):
        for number in range(2, 12):
            new_deck.append(Card(suit, number))
        for _ in range(4):
            new_deck.append(Card(suit, 10))
    return new_deck

def take_card (player):
    new_card = random.choice(deck)
    player.append(new_card)
    deck.remove(new_card)

def total_score (player):
    score = 0
    ace_check = False
    for num, elem in enumerate(player):
        score += elem.number
        if elem.number == 11:
            ace_check = True
            ace_card = num
    if score > 21 and ace_check:
        player[ace_card].number = 1
        score = total_score(player)
    return score


deck = deck_builder()

player_hand = []
player_score = 0
diller_hand = []
diller_score = 0

for _ in range (2):
    take_card(player_hand)
    take_card(diller_hand)

print ('We start the game!')
command = 'start'
while command != 'stop':
    print('\nYour hand:')
    for num, elem in enumerate(player_hand):
        print(elem.suit, elem.number)
    player_score = total_score(player_hand)
    print('\nYour total score:', player_score)
    print('\nWhat are you going to do? take or stop?')
    if player_score > 21:
        break
    command = input('').lower()
    if command == 'take':
        take_card(player_hand)
    elif command != 'stop':
        print('\nI don not understand you')

while diller_score < 17:
    diller_score = total_score(diller_hand)
    if diller_score < 17:
        take_card(diller_hand)

print('\nYour score:', player_score)
print('\nDiller hand:')
for num, elem in enumerate(diller_hand):
    print(elem.suit, elem.number)
print('\nDiller score:', diller_score)

if player_score < 22 and player_score > diller_score \
        or player_score < 22 and diller_score > 21:
    print ('\nYou won!')
elif player_score < 22 and player_score == diller_score:
    print('\nPush! Nobody win')
else:
    print('\nYou lose!')











