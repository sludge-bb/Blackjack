import random
import time

def calculate_total(hand):
    total = sum(values[i] for i in hand)
    aces = hand.count(12)

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
player_hand = []
dealer_hand = []

deck = list(range(13)) * 4
random.shuffle(deck)

print("""
██████  ██       █████   ██████ ██   ██      ██  █████   ██████ ██   ██ 
██   ██ ██      ██   ██ ██      ██  ██       ██ ██   ██ ██      ██  ██  
██████  ██      ███████ ██      █████        ██ ███████ ██      █████   
██   ██ ██      ██   ██ ██      ██  ██  ██   ██ ██   ██ ██      ██  ██  
██████  ███████ ██   ██  ██████ ██   ██  █████  ██   ██  ██████ ██   ██""")
print("""
┌┬┐┌─┐╶┬┐┌─╴   ┌┐ ╷ ╷   ┌─┐╷  ╷ ╷╶┬┐┌─╴┌─╴   ┌┐ ┌┐ 
│││├─┤ ││├╴    ├┴┐└┬┘   └─┐│  │ │ │││╶┐├╴    ├┴┐├┴┐
╵ ╵╵ ╵╶┴┘└─╴   └─┘ ╵    └─┘└─╴└─┘╶┴┘└─┘└─╴╶─╴└─┘└─┘""")

player_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
dealer_hand.append(deck.pop())

player_total = calculate_total(player_hand)
dealer_total = calculate_total(dealer_hand)

time.sleep(0.5)
print("\n")
print("Your turn")
time.sleep(0.5)
print(f"Your hand: [{cards[player_hand[0]]}, {cards[player_hand[1]]}] -> Total: {player_total}")
print("\n")

while True:
    if player_total < 21:
        choice = input("(H)it or (S)tay: ").upper()
        if choice == "H":
            player_hand.append(deck.pop())
            raw_total = sum(values[i] for i in player_hand)
            player_total = calculate_total(player_hand)
            print(f"Drew: {cards[player_hand[-1]]}")
            print(f"Your hand: [{', '.join(cards[i] for i in player_hand)}] -> Total: {player_total}")
            print("\n")

            if raw_total > 21 and player_total <= 21:
                time.sleep(0.5)
                print(f"Your Ace is now worth 1.")
                print("\n")

        elif choice == "S":
            break
        else:
            print("That is not a valid option. ", end = "")
    elif player_total == 21:
        if len(player_hand) == 2:
            print("Blackjack!")
        else:
            print("21!")
        break
    else:  
        print("Bust! You lose!")
        break

if player_total < 22:
    time.sleep(1)
    print("\n")
    print("Dealer's turn")
    time.sleep(0.5)
    print(f"Dealer's hand: [{cards[dealer_hand[0]]}, {cards[dealer_hand[1]]}] -> Total: {dealer_total}")
    print("\n")
    time.sleep(1)
    while True:
        if dealer_total < 21:
            hit_chance = min(1.0, (21 - dealer_total) / 10)
            if dealer_total < player_total:
                hit_chance = min(1.0, hit_chance + 0.25)
            if random.random() < hit_chance:
                dealer_hand.append(deck.pop())
                raw_total = sum(values[i] for i in dealer_hand)
                dealer_total = calculate_total(dealer_hand)
                print(f"Dealer hits and draws {cards[dealer_hand[-1]]}.")
                time.sleep(0.5)
                print(f"Dealer's hand: [{', '.join(cards[i] for i in dealer_hand)}] -> Total: {dealer_total}")
                print("\n")
                if raw_total > 21 and dealer_total <= 21:
                    time.sleep(0.5)
                    print(f"Dealer's Ace is now worth 1.")
                    print("\n")
                time.sleep(1)
            else:
                print("Dealer stands!")
                if dealer_total > player_total:
                    print("Dealer wins!")
                    break
                elif dealer_total < player_total:
                    print("You win!")
                    break
                else:
                    print("Tie!")
                    break                    
        elif dealer_total == 21:
            if player_total == 21:
                if len(dealer_hand) == 2:
                    print("Blackjack! Tie!")
                else:
                    print("21! Tie!")
                break
            else:
                if len(dealer_hand) == 2:
                    print("Blackjack! You lose!")
                else:
                    print("21! You lose!")
                break
        else:
            print("Bust! You win!")
            break