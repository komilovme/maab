# =================
# Questions
# =================

# answer-1 Loops quiz
# (External quiz link – conceptual task, code not required)

# answer-2 Difference between continue and break

# BREAK example
for i in range(5):
    if i == 2:
        break
    print(i)

# CONTINUE example
for i in range(5):
    if i == 2:
        continue
    print(i)


# answer-3 Difference between for and while

# FOR loop
for i in range(3):
    print(i)

# WHILE loop
i = 0
while i < 3:
    print(i)
    i += 1


# answer-4 Nested for loop example
for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end=" ")
    print()


# =================
# Homework-1
# Return uncommon elements
# =================

list1 = [1, 1, 2]
list2 = [2, 3, 4]

result = []

for x in list1:
    if x not in list2:
        result.append(x)

for x in list2:
    if x not in list1:
        result.append(x)

result


# =================
# Homework-2
# Squares less than n
# =================

n = 5

for i in range(1, n):
    print(i ** 2)


# =================
# Homework-3
# Add underscore rule
# =================

txt = "hello"
result = ""
count = 0
vowels = "aeiouAEIOU"

i = 0
while i < len(txt):
    result += txt[i]
    count += 1

    if count == 3:
        if i != len(txt) - 1:
            if txt[i] in vowels:
                count = 2
            else:
                result += "_"
                count = 0
    i += 1

result


# =================
# Homework-4
# Number Guessing Game
# =================

import random

number = random.randint(1, 100)
attempts = 10

while attempts > 0:
    guess = int(input("Enter guess: "))
    attempts -= 1

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("You guessed it right!")
        break
else:
    print("You lost. Want to play again?")


# =================
# Homework-5
# Password Checker
# =================

password = input("Enter password: ")

if len(password) < 8:
    print("Password is too short.")
elif not any(c.isupper() for c in password):
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")


# =================
# Homework-6
# Prime Numbers 1-100
# =================

for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


# =================
# Bonus
# Rock Paper Scissors
# =================

import random

choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while player_score < 5 and computer_score < 5:
    player = input("Choose rock/paper/scissors: ").lower()
    computer = random.choice(choices)

    if player not in choices:
        print("Invalid choice")
        continue

    print("Computer:", computer)

    if player == computer:
        print("Draw")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win this round")
        player_score += 1
    else:
        print("Computer wins this round")
        computer_score += 1

    print("Score:", player_score, "-", computer_score)

if player_score == 5:
    print("You won the match!")
else:
    print("Computer won the match!")
