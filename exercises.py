# Exercise 1: Vowel or Consonant
vowel = ['a', 'e', 'o', 'u', 'i']
def check_letter():
    user_input = input('enter a letter (a-z or A-Z): ')

    if user_input in vowel:
        print(f'The letter {user_input} is a vowel')
    else: 
        print(f'The letter {user_input} is a consonant')

# Call the function
# check_letter()

# Exercise 2: Old enough to vote?
def check_voting_eligibility():
    user_age = int(input('Please enter your age: '))
    vote_age = 50

    if user_age < 50:
        print('you can vote')
    else: 
        print('you are not allowed to vote')

# Call the function
# check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    dog_age = int(input("Input a dog's age: "))

    if dog_age <= 0:
        print('the age must be postive')
        return
    if dog_age == 1: 
        dog_age = 10
    elif dog_age == 2:
        dog_age = 20
    else: 
        dog_age = 20 + (dog_age -2)* 7
    print(f'the dog age is {dog_age}')
        
    


# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
def weather_advice():
    is_cold = input('it is cold (yes/no): ').lower()
    is_raining = input('it is raining (yes/no): ').lower()

    if is_cold == 'yes' and is_raining == 'yes':
        print('Wear a waterproof coat')
    elif is_cold == 'yes' and is_raining == 'no':
        print('Wear a warm coat')
    elif is_raining == 'yes' and is_cold == 'no':
        print('Carry an umbrella')
    else:
        print('Wear light clothing')

# Call the function
# weather_advice()


# Exercise 5:
def fizz_buzz():
    for i in range(1,50):
        if(i%3 == 0 and i%5 == 0):
            print('FizzBuzz')
        elif(i%3 == 1):
            print('Fizz')
        elif(i%5 == 1):
            print('Buzz')

# Call the function
# fizz_buzz()