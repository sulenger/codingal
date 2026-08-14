import random

x = random.random()
print(x)



import random

letters = ['A', 'B', 'C', 'D', 'E']

# Picks one random letter from the list
random_letter = random.choice(letters)

print("Picked letter:", random_letter)



import random

random.seed(20)  # Switch to Channel 20

print(random.randint(1, 10))  # Will ALWAYS be 3
print(random.randint(1, 10))  # Will ALWAYS be 5

