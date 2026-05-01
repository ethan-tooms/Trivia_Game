# Ethan Tooms
# Trivia Game

import random

# Trivia questions and answers
trivia = {
    'What is the capitol of the United States?': 'Washington D.C.',
    'What is the largest planet in our solar system?': 'Jupiter',
    'What is the smallest country in the world?': 'Vatican City',
    'What is the fastest bird in the world?': 'Peregrine Falcon'
}

def game_start():
    # Select a random question/answer pair
    question = random.choice(list(trivia.keys()))
    answer = trivia[question]

    print(question)
    user_answer = input("Your answer: ")

    if user_answer.lower().strip() == answer.lower().strip():
        print('Correct!')
    else:
        print(f'Incorrect! The correct answer was {answer}.')

print("Welcome to trivia!")

start = input("Do you want to play? (y/n): ")

# Validate user input
while start.lower().strip() != 'y' and start.lower().strip() != 'n':
    start = input("Please enter \'y\' or \'n\': ")

if start.lower().strip() == 'n':
    print("Have a good day!")
    quit()
else:
    print("Let\'s get this started!")
    game_start()