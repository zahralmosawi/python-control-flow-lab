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