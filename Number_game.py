import random

print("=== Number Guess Game === 🎯")
print("1-100 athara number ekak hadala tiyenawa\n")

secret = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Oya guess kare mona number da? "))
    tries += 1
    
    if guess == secret:
        print(f"\nPATTA MACHAN! {tries} try walin haduna! 💪")
        break
    elif guess < secret:
        print("Wadida → Uda yapan")
    else:
        print("Wadida → Passe yapan")
