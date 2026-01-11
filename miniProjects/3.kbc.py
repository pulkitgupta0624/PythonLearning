'''
Create a program capable of displaying question to the user like KBC (kaun banega crorepati).
use list data type to store the questions and their correct answers.
Display the final amount the person is taking home after playing the game.
'''
# List of questions with options and correct answer
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
        "correct": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "correct": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific"],
        "correct": "D"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A) Mark Twain", "B) William Shakespeare", "C) Jane Austen", "D) Charles Dickens"],
        "correct": "B"
    }
]

# Prize amounts for each correct answer
prize_money = [10000, 50000, 100000, 1000000]

# Game logic
amount = 0
for i, q in enumerate(questions):
    print(f"\nQuestion {i+1}: {q['question']}")
    for option in q['options']:
        print(option)
    
    answer = input("Your answer (A/B/C/D): ").upper()
    
    if answer == q['correct']:
        amount = prize_money[i]
        print(f"Correct! You've won ₹{amount}")
    else:
        print(f"Wrong! The correct answer was {q['correct']}")
        break

print(f"\nYou are taking home: ₹{amount}")

