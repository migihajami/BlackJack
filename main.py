import art
import shuffle



decks = shuffle.stir(1)

print(art.logo)
print("Welcome to the table! Black Jack 21. Dealer must hit on 16 and stop on 17.")

print(len(decks))
print(decks)

response = input("More?")
      