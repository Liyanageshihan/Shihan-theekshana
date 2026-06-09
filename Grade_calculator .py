name = input("Oyage name eka mokadada? ")
k1 = int(input("1st mark: "))
k2 = int(input("2nd mark: "))
k3 = int(input("3rd mark: "))

average = (k1 + k2 + k3) / 3
print(f"\n{name}, oyage average: {average:.2f}")

if average >= 75:
    print("Grade: A - Patta machan! 💪")
elif average >= 50:
    print("Grade: C - Pass kale! Yanawa")
else:
    print("Grade: F - Next time try karamu")
